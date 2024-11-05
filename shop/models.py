from django.db import models
from system_settings.models import Organization
from django.conf import settings

# Represents the product categories available in the marketplace. 
# This table will store all the categories that are common to all museums.
# class Category(models.Model):
#     title = models.CharField(max_length=255)
#     is_main = models.BooleanField(default=False)
#     image = models.ImageField(upload_to='product_category/image')

#     # Add any additional fields for the category

#     def __str__(self):
#         return self.title

#     class Meta:
#         db_table = 'category'
#         verbose_name = 'Категория продуктов'
#         verbose_name_plural = 'Категории продуктов'

# Represents the product categories specific to each museum. 
# This table will store the categories unique to each museum.
class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    is_main = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product_category/image')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='product_categories')
   
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)
        
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'product_category'
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'  


# Product
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_recommended = models.BooleanField(default=False)
    main_image = models.ImageField(upload_to='product/image')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, related_name='products')
    price = models.FloatField(default=0.0)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def main_image_url(self):
        if self.main_image:
            return "%s%s" % (settings.HOST, self.main_image.url)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты' 


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product/other_images')

    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)
        
    def __str__(self):
        return self.image.url
    

    class Meta:
        db_table = 'products_image'
        verbose_name = 'Изображение продуктов'
        verbose_name_plural = 'Изображения продуктов' 