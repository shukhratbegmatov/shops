from modeltranslation.translator import TranslationOptions, register
from system_settings.models import CompanyInfo, Menu, Organization

@register(CompanyInfo)
class CompanyInfoTranslationOptions(TranslationOptions):
    fields = (
        'logo_title', 'company_description', 
    )

@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = (
        'title', 
    )

@register(Organization)
class OrganizationTranslationOptions(TranslationOptions):
    fields = (
        'title', 
    )