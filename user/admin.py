from django.contrib import admin
from .models import User


# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'role')
    list_display_links = ("id", 'first_name')
