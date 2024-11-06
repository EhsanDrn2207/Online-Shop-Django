from django.contrib import admin

from .models import Product, Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['user', 'body', 'stars', 'is_active']
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active']
    ordering = ('price', )
    inlines = [CommentsInline]


admin.site.register(Product, ProductAdmin)


class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'is_active', 'is_recommend']


admin.site.register(Comment, ProductCommentAdmin)
