from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active']
    ordering = ('price', )


admin.site.register(Product, ProductAdmin)
