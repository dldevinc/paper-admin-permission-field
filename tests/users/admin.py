from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from paper_permission_field.forms import PermissionField


class CustomUserChangeForm(UserChangeForm):
    user_permissions = PermissionField(
        required=False,
    )


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
