from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from account.permissions import IsMuseumAdmin
from rest_framework.generics import get_object_or_404

from .models import ContactUs, CompanyInfo, Menu, Organization
from .serializers import CompanyInfoHeaderSerializer, MenuSerializer, CompanyInfoFooterSerializer, ContactUsSerializer, \
                        OrganizationMuseumAdminSerializer, OrganizationSerializer

class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'title'):
            queryset = self.queryset.exclude(title__exact='')
        
        return queryset
    

class HeaderView(CustomModalViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = MenuSerializer
    pagination_class = None
    http_method_names = ['get']


    def list(self, request, *args, **kwargs):
        is_market = request.query_params.get('is_market')
        if is_market == '1':
            menus = Menu.objects.filter(is_main=True)
        else:
            menus = Menu.objects.filter(is_main=False)
        company = self.get_queryset().last()
        menu_serializer = self.serializer_class
        company_serializer = CompanyInfoHeaderSerializer
        payload = {
            'company_info': company_serializer(company).data,
            'menus': menu_serializer(menus, many=True).data,
        }
        return Response(payload)
    

class FooterView(CustomModalViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoFooterSerializer    
    pagination_class = None
    http_method_names = ['get']


    def list(self, request, *args, **kwargs):
        company_info = self.get_queryset().last()
        contact_details = ContactUs.objects.all().last()
        company_info_serializer = self.get_serializer_class()
        contact_details_serializer = ContactUsSerializer
        payload = {
            'company_info': company_info_serializer(company_info).data,
            'contact_details': contact_details_serializer(contact_details).data
        }
        return Response(payload)
    

class OrganizationMuseumAdminView(CustomModalViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationMuseumAdminSerializer    
    permission_classes = (IsMuseumAdmin, )
    authentication_classes = (JWTAuthentication, )
    pagination_class = None
    http_method_names = ['get']

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.organization.id)
    

class OrganizationView(CustomModalViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer    
    http_method_names = ['get']
    lookup_field = 'subdomain_field'

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj
    
    def get_queryset(self):
        subdomain = self.request.query_params.get('subdomain', None)
        if subdomain is not None:
            queryset = self.queryset.filter(subdomain_field=subdomain)
            return queryset
        return self.queryset
