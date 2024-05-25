from django import forms
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Group, Permission, User

from paper_permission_field.forms import PermissionsField


class GroupAdminForm(forms.ModelForm):
    permissions = PermissionsField(
        required=False,
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = forms.ALL_FIELDS


class CustomUserChangeForm(UserChangeForm):
    user_permissions = PermissionsField(
        required=False,
        queryset=Permission.objects.all()
    )


class CustomGroupAdmin(GroupAdmin):
    form = GroupAdminForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Group, CustomGroupAdmin)
