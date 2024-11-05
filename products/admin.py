from django.contrib import admin

from .models import Product, Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active']
    ordering = ('price', )


admin.site.register(Product, ProductAdmin)


class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'is_active', 'is_recommend']


admin.site.register(Comment, ProductCommentAdmin)
