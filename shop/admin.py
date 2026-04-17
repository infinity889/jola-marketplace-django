from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class categoryadmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class productadmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'slug', 'image', 'description', 'price', 'available', 'created', 'updated']
    list_filter = ['created', 'updated', 'available', 'category']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'available']
