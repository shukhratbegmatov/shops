from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import CustomUser
from phonenumber_field.serializerfields import PhoneNumberField
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate
from .exceptions import (
    AccountNotRegisteredException,
    InvalidCredentialsException,
    AccountDisabledException,
)

from phonenumber_field.serializerfields import PhoneNumberField

# Password field for tokenobtainserializer
class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("style", {})

        kwargs["style"]["input_type"] = "password"
        kwargs["write_only"] = True

        super().__init__(*args, **kwargs)


# BaseClass for token serializer with phone number and password or email and password
class TokenObtainSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = PasswordField()
    token_class = None

    def _validate_email(self, email, password):
        self.user = None

        if email and password:
            self.user = authenticate(username=email, password=password)
        else:
            raise serializers.ValidationError(
                _("Enter an email and password."))

        return self.user

    def validate(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')

        self.user = None
        self.user = self._validate_email(email, password)

        if not self.user:
            raise InvalidCredentialsException()

        if not self.user.is_active:
            raise AccountDisabledException()
           
        return {}
    
    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)
    

class MuseumAdminLogInSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)
        
        refresh = self.get_token(self.user)

        data['user_id'] = self.user.id
        data['role'] = self.user.role
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data
    

class MuseumAdminInfoSerializer(serializers.ModelSerializer):
    organization_title = serializers.CharField(source='organization.title')

    class Meta:
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number', 'profile_image_url', 'role',
            'organization', 'organization_title'
        ]
        model = CustomUser


class CustomerLogInSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)
        
        refresh = self.get_token(self.user)

        data['user_id'] = self.user.id
        data['role'] = self.user.role
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data
    

# Sign up with email and password or phone_number and password
class CustomerSignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


class VerificationSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=555)

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    guid = serializers.UUIDField()

    def validate(self, attrs):
        password = attrs["password"]
        confirm_password = attrs["confirm_password"]
        if password != confirm_password:
            raise serializers.ValidationError("passwords do not match")
        return attrs
    
    
class CustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number', 'profile_image_url', 'role'
        ]
        model = CustomUser