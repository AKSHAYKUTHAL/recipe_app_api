"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name','is_active','is_staff']
    list_editable = ['is_active','is_staff'] 

    fieldsets = (
        (None, {
            'fields': ('email', 'password')}),

        (_('Personal Info'), {
            'fields': ('name',)}),

        (_('Permissions'),{
            'fields': ('is_active','is_staff','is_superuser',)}),

        (_('Important dates'), {
            'fields': ('last_login',)}),
    )

    readonly_fields = ['last_login']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),# adds a css class wide, which makes a slight differences for certain fields style
            'fields': ('email','password1','password2','name','is_active','is_staff','is_superuser',),}),
    )


admin.site.register(User, UserAdmin)
# admin.site.register(models.Recipe)
# admin.site.register(models.Tag)
# admin.site.register(models.Ingredient)
# class UserAdmin(admin.ModelAdmin):

