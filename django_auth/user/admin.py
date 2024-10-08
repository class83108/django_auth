from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import MyUser


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ("username", "email", "phone")

    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1] = (
        _("Personal info"),
        {"fields": ("first_name", "last_name", "email", "phone")},
    )
