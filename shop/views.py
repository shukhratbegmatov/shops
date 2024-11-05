from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import MethodNotAllowed
from account.permissions import IsMuseumAdmin

from .models import ProductCategory, Product, ProductImage
from system_settings.models import Organization
from .serializers import ProductCategoryMuseumAdminListSerializer, ProductCategoryMuseumAdminDetailSerializer, \
                        ProductMuseumAdminListSerializer, ProductImagesMuseumAdminSerializer, ProductMuseumAdminDetailSerializer, \
                        IndexProductSerializer, RecommendedProductSerializer, IndexProductCategorySerializer, ProductCategorySerializer, \
                        ProductDetailSerializer, ProductListSerializer

from . import pagination

# Create your views here.
class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'title'):
            queryset = self.queryset.exclude(title__exact='')
        
        return queryset
    

# Product Category & Museum Admin
class ProductCategoryModelViewSet(CustomModalViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryMuseumAdminListSerializer
    pagination_class = None
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsMuseumAdmin,)

    def get_queryset(self):
        queryset = ProductCategory.objects.filter(organization=self.kwargs['organization_pk'])
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializer_class
        return ProductCategoryMuseumAdminDetailSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        organization_id = kwargs.get('organization_pk')
        organization = Organization.objects.get(pk=organization_id)
        serializer.validated_data['organization'] = organization

        self.perform_create(serializer)

        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        organization_id = kwargs.get('organization_pk')
        organization = Organization.objects.get(pk=organization_id)
        serializer.validated_data['organization'] = organization

        self.perform_update(serializer)

        return Response(serializer.data)
    

# Product & Museum Admin
class ProductModelViewSet(CustomModalViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductMuseumAdminListSerializer
    pagination_class = None
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsMuseumAdmin,)

    def get_queryset(self):
        queryset = Product.objects.filter(category=self.kwargs['category_pk'])
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializer_class
        return ProductMuseumAdminDetailSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category_id = kwargs.get('category_pk')
        organization_id = kwargs.get('organization_pk')

        organization = Organization.objects.get(pk=organization_id)
        category = ProductCategory.objects.get(pk=category_id)

        serializer.validated_data['category'] = category
        serializer.validated_data['organization'] = organization

        self.perform_create(serializer)
        product_images = request.FILES.getlist('images')
        if product_images:
            for image_data in product_images:
                product_id = serializer.data.get('id')
                product = Product.objects.get(id=product_id)
                ProductImage.objects.create(product=product, image=image_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        category_id = kwargs.get('category_pk')
        organization_id = kwargs.get('organization_pk')

        organization = Organization.objects.get(pk=organization_id)
        category = ProductCategory.objects.get(pk=category_id)

        serializer.validated_data['category'] = category
        serializer.validated_data['organization'] = organization

        self.perform_update(serializer)

        product_images = request.FILES.getlist('images')
        product_id = serializer.data.get('id')
        product = Product.objects.get(id=product_id)
        ProductImage.objects.filter(product=product).delete()
        if product_images:
            for image_data in product_images:
                ProductImage.objects.create(product=product, image=image_data)
        return Response(serializer.data)
    

# New Product & Organization
class IndexProductByOrganizationView(CustomModalViewSet):
    queryset = Product.objects.all()
    serializer_class = IndexProductSerializer
    http_method_names = ['get']
    pagination_class = None

    def get_queryset(self):
        queryset = Product.objects.filter(organization__subdomain_field=self.kwargs['organization_subdomain_field']).order_by('-created_at')[:8]
        return queryset
    

# Index Product Category & Organization
class IndexProductCategoryByOrganizationView(CustomModalViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = IndexProductCategorySerializer
    http_method_names = ['get']
    pagination_class = None

    def get_queryset(self):
        queryset = ProductCategory.objects.filter(organization__subdomain_field=self.kwargs['organization_subdomain_field'], is_main=True)
        return queryset


# Product Category & Organization
class ProductCategoryByOrganizationView(CustomModalViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    http_method_names = ['get']
    pagination_class = None

    def get_queryset(self):
        queryset = ProductCategory.objects.filter(organization__subdomain_field=self.kwargs['organization_subdomain_field'])
        return queryset
    

# Product & Organization
class ProductByOrganizationView(CustomModalViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    http_method_names = ['get']
    pagination_class = pagination.MidShort
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__title']

    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializer_class
        else:
            return ProductDetailSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(organization__subdomain_field=self.kwargs['organization_subdomain_field'])
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        related = self.get_queryset().filter(category=instance.category, organization=instance.organization).exclude(id=instance.id,)[:4]
        payload = {
            'product': self.get_serializer(instance).data,
            'related': self.serializer_class(related, many=True).data
        }
        return Response(payload)


# New Product & Organization
class RecommendedProductByOrganizationView(CustomModalViewSet):
    queryset = Product.objects.all()
    serializer_class = RecommendedProductSerializer
    http_method_names = ['get']
    pagination_class = None

    def get_queryset(self):
        queryset = Product.objects.filter(organization__subdomain_field=self.kwargs['organization_subdomain_field'], is_recommended=True).order_by('-created_at')[:16]
        return queryset

# New Product
class IndexProductView(CustomModalViewSet):
    queryset = Product.objects.all()
    serializer_class = IndexProductSerializer
    http_method_names = ['get']
    pagination_class = None

    def get_queryset(self):
        queryset = Product.objects.all().order_by('-created_at')[:8]
        return queryset
    
# Product
class ProductView(CustomModalViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    http_method_names = ['get']
    pagination_class = None

    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET')
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        related = self.get_queryset().filter(category=instance.category, organization=instance.organization).exclude(id=instance.id,)[:4]
        payload = {
            'product': self.get_serializer(instance).data,
            'related': self.serializer_class(related, many=True).data
        }
        return Response(payload)

    
# Recommended Product
class RecommendedProductView(CustomModalViewSet):
    queryset = Product.objects.all()
    serializer_class = RecommendedProductSerializer
    http_method_names = ['get']
    pagination_class = None

    def get_queryset(self):
        queryset = Product.objects.filter(is_recommended=True).order_by('-created_at')[:4]
        return queryset