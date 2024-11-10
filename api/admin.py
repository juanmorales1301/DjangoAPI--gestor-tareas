# api/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user import CustomUser
from .models.post import Post

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets
    search_fields = ['username', 'email']
    ordering = ['username']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)
