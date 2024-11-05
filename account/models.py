from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager
from system_settings.models import Organization

AVATAR = [800, 600]


class CustomUser(AbstractUser):
    Superadmin = 1
    Museum_Admin = 2
    Customer = 3

    role_choice = (
        (Superadmin, 'Суперадмин'),
        (Museum_Admin, 'Админ музея'),
        (Customer, 'Пользователь'),
    )

    username = None
    profile_image = ResizedImageField(upload_to='users/', size=AVATAR, blank=True, null=True)
    role = models.IntegerField(choices=role_choice, default=0)
    email = models.EmailField(
        _('email address'), unique=True, blank=True, null=True
        )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = PhoneNumberField(
        _("Phone number"),
        unique=True,
        help_text=_("Required. Only international format used."),
        error_messages={
            "unique": _("User with this phone number already exists.")
        },
        blank=True,
        null=True,
    )
        
    @property
    def profile_image_url(self):
        if self.profile_image:
            return "%s%s" % (settings.HOST, self.profile_image.url)
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'custom_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
