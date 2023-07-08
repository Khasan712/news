from django.contrib import admin
from .models import (
    New,
    Category,
    Image,
    Blog
)


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'category', 'created_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", 'title')



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", 'new', 'blog','image')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'creator', 'seen_qty', 'created_at')
