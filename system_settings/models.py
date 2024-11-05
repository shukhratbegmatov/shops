from django.db import models
from django.conf import settings

# Create your models here.
class ContactUs(models.Model):
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    instagram = models.URLField()
    facebook = models.URLField()
    telegram = models.URLField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Контакты"
    
    class Meta:
        db_table = 'contact_us'
        verbose_name = 'Свяжитесь с нами'
        verbose_name_plural = 'Свяжитесь с нами'


class CompanyInfo(models.Model):
    logo_title = models.CharField(max_length=255)
    logo = models.FileField(upload_to='company/logo')
    company_description = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def logo_url(self):
        if self.logo:
            return "%s%s" % (settings.HOST, self.logo.url)
        

    def __str__(self):
        return "Информация о проекте"
    
    class Meta:
        db_table = 'company_info'
        verbose_name = 'Информация о проекте'
        verbose_name_plural = 'Информация о проекте'


class Menu(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=500, null=True)
    is_main = models.BooleanField(default=False)
    order = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'menu'
        ordering = ['order']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'  


class Organization(models.Model):
    title = models.CharField(max_length=255)
    logo = models.FileField(upload_to='organization/logo', blank=True, null=True)
    subdomain_field = models.SlugField(max_length=200, default='')
    file = models.FileField(upload_to='organization/file')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def logo_url(self):
        if self.logo:
            return "%s%s" % (settings.HOST, self.logo.url)

    @property
    def file_url(self):
        if self.file:
            return "%s%s" % (settings.HOST, self.file.url)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'organization'
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'  