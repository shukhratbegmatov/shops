from rest_framework import serializers
from .models import ProductCategory, Product, ProductImage


class ProductCategoryMuseumAdminListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = [
            'id', 'title', 'created_at', 'image_url'
        ]


class ProductCategoryMuseumAdminDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = [
            'id', 'title', 'image', 'is_main', 'image_url'
        ]


class ProductMuseumAdminListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'created_at', 'main_image_url'
        ]


class ProductImagesMuseumAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = [
            'id', 'image', 'image_url'
        ]


class ProductMuseumAdminDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ProductImage.objects.filter(product=obj.id)
        return ProductImagesMuseumAdminSerializer(images, many=True).data
    
    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'is_recommended', 'main_image', 'main_image_url', 'price', 'images'
        ]


class IndexProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'price', 'main_image_url'
        ]
    

class RecommendedProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'main_image_url', 'price'
        ]


class IndexProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = [
            'id', 'title', 'image_url'
        ]


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = [
            'id', 'title',
        ]


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'price', 'main_image_url'
        ]

class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = [
            'id', 'image_url'
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = ProductImage.objects.filter(product=obj.id)
        return ProductImageSerializer(images, many=True).data
    
    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'main_image_url', 'price', 'images'
        ]

    