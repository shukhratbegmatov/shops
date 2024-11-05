import uuid

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.template.loader import render_to_string
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
import jwt
from .utils import Util
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http.response import Http404
from django.core.cache import cache

from .serializers import MuseumAdminInfoSerializer, MuseumAdminLogInSerializer, CustomerLogInSerializer, CustomerSignUpSerializer, \
                        VerificationSerializer, ForgotPasswordSerializer, ResetPasswordSerializer, CustomerInfoSerializer
from .models import CustomUser
from .permissions import IsMuseumAdmin

def set_cache(key, val, ttl=300):
    cache.set(f"{key}", val, timeout=ttl)

def generate_uuid():
    return uuid.uuid4()

# EMAIL
def email_constuctor(user_token):
    emailSubject = "Emailni tasdiqlash"
    current_site = settings.FRONTEND
    relative_url = 'users/email-verify'
    absolute_url = current_site + '/' + relative_url + "?token=" + str(user_token)
    context = ({"absolute_url": absolute_url})
    html_content = render_to_string('email_confimation.html', context)

    return emailSubject, html_content

def reset_password_email_constructor(user_token):
    emailSubject = "Parolni tiklash"
    current_site = settings.FRONTEND
    relative_url = 'users/password-reset'
    absolute_url = current_site + '/' + relative_url + "?token=" + str(user_token)
    context = ({"absolute_url": absolute_url})
    html_content = render_to_string('password_reset.html', context)

    return emailSubject, html_content


class MuseumAdminLogOutView(APIView):
    permission_classes = (IsMuseumAdmin, )
    

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MuseumAdminLogInView(TokenObtainPairView):
    serializer_class = MuseumAdminLogInSerializer


class GetMuseumAdmin(APIView):
    serializer_class = MuseumAdminInfoSerializer
    permission_classes = (IsMuseumAdmin, )
    authentication_classes = (JWTAuthentication, )

    def get(self, request, *args, **kwargs):
        self.object = get_object_or_404(CustomUser, pk=request.user.id)
        serializer = self.serializer_class(self.object)
        return Response(serializer.data)
    

class CustomerLogOutView(APIView):
    permission_classes = (IsAuthenticated,)
    

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class CustomerLogInView(TokenObtainPairView):
    serializer_class = CustomerLogInSerializer


class CustomerRegisterView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        email = request.data.get('email', None)
        serializer = CustomerSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        data['is_active'] = False
        password = data['password']
        if email :
            instance, created = CustomUser.objects.get_or_create(
                email=email, first_name=data['first_name'], last_name=data['last_name'],
                is_active=data['is_active'], role=CustomUser.Customer
                )
        instance.set_password(password)
        instance.save(update_fields=["password"])
        if created:
            token = RefreshToken.for_user(instance).access_token
            email_subject, html_content = email_constuctor(token)
            Util.send_email(email_subject=email_subject, sender=settings.EMAIL_HOST_USER, receiver=instance.email, html_content=html_content)
            return Response(data={"success": "email is sent"}, status=status.HTTP_201_CREATED)
        else:
            if not instance.is_active:
                token = RefreshToken.for_user(instance).access_token
                email_subject, html_content = email_constuctor(token)   
                Util.send_email(email_subject=email_subject, sender=settings.EMAIL_HOST_USER, receiver=instance.email, html_content=html_content)
                return Response(data={"success": "email is sent"}, status=status.HTTP_302_FOUND)
            else:
                return Response(
                    data={"error": f"{data['email']} is taken."},
                    status=status.HTTP_409_CONFLICT,
                )
            

class CustomerVerifyView(APIView):
    serializer_class = VerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def post(self, request):
        serializer = VerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.POST.get('token', None)
        if token:
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                user = get_object_or_404(CustomUser, id=payload['user_id'])
                if not user.is_active:
                    user.is_active = True
                    user.save()
                return Response(data={'success': 'Account is successfully activated with email'}, status=status.HTTP_200_OK)
            except jwt.ExpiredSignatureError as identifier:
                return Response(data={'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
            except jwt.exceptions.DecodeError as identifier:
                return Response(data={'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"error": "Please provide token"}, status=status.HTTP_400_BAD_REQUEST)
        

class CustomerForgotPasswordView(APIView):
    permission_classes = (AllowAny, )


    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.POST.get('email', None)
        
        if email:
            instance = get_object_or_404(CustomUser, email=email)
            token = RefreshToken.for_user(instance).access_token
            email_subject, html_content = reset_password_email_constructor(token)
            Util.send_email(email_subject=email_subject, sender=settings.EMAIL_HOST_USER, receiver=instance.email, html_content=html_content)
            return Response(data={"success": "email is sent"}, status=status.HTTP_302_FOUND)
        else:
            return Response(data={"error": "Please provide email or phone_number"}, status=status.HTTP_400_BAD_REQUEST)
        

class CustomerVerifyResetPasswordView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = VerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.POST.get('token', None)
        if token:
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                instance = get_object_or_404(CustomUser, id=payload['user_id'])
                guid = generate_uuid()
                set_cache(key=guid, val=instance.email, ttl=86400)
                return Response(data={"guid": guid}, status=status.HTTP_200_OK)
            except jwt.ExpiredSignatureError as identifier:
                return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
            except jwt.exceptions.DecodeError as identifier:
                return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"error": "Please provide token"}, status=status.HTTP_400_BAD_REQUEST)
        

class CustomerResetPasswordView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        email = cache.get(data['guid'])
        if email is None:
            return Response(data={"error": "something wrong with guid"}, status=status.HTTP_400_BAD_REQUEST)
        instance = CustomUser.objects.get(email=email)
        instance.set_password(data['password'])
        instance.save()
        cache.expire(data["guid"], timeout=1)
        return Response(data={"success": "password is resetted successfully"}, status=status.HTTP_200_OK)
        

class CustomerGetMe(APIView):
    serializer_class = CustomerInfoSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )

    def get(self, request, *args, **kwargs):
        self.object = get_object_or_404(CustomUser, pk=request.user.id)
        serializer = self.serializer_class(self.object)
        return Response(serializer.data)