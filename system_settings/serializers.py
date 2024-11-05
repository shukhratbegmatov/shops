from rest_framework import serializers
from .models import ContactUs, CompanyInfo, Menu, Organization

class CompanyInfoHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = [
            'logo_title', 'logo_url'
        ]

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = [
            'id', 'title', 'url', 'order', 'is_main'
            ]
        

class CompanyInfoFooterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyInfo
        fields = [
            'logo_title', 'logo_url', 'company_description'
        ]


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = [
            'phone_number', 'email', 'instagram', 'facebook', 'telegram'
        ]


class OrganizationMuseumAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = [
            'id', 'title'
        ]


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = [
            'id', 'title', 'logo_url', 'subdomain_field', 'file_url'
            ]