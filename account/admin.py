from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'phone_number', 'first_name', 'last_name', 'is_staff')
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'organization', 'phone_number', 'role', 'profile_image'),
    }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number', 'organization', 'role', 'profile_image')}),
        (_('Permissions'), {
        'fields': ('is_active', 'is_staff', 'is_superuser'),
    }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
)


class OutstandingTokenAdmin(OutstandingTokenAdmin):
    def has_delete_permission(self, *args, **kwargs):
        return True # or whatever logic you want
    
    def get_actions(self, request):
        actions = super(OutstandingTokenAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(OutstandingToken)
admin.site.register(OutstandingToken, OutstandingTokenAdmin)