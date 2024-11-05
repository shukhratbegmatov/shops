from django.contrib import admin
from .models import ProductImage, Product, ProductCategory

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)