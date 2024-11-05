from modeltranslation.translator import TranslationOptions, register
from shop.models import ProductCategory, Product

@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        'title', 'description',
    )

