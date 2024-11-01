from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUserModel


class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )
    list_display = ('username', 'email', 'is_staff', 'is_active')


admin.site.register(CustomUserModel, CustomUserAdmin)
