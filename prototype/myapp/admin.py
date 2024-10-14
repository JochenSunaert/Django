# myapp/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Article

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article)