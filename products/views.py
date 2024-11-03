from django.shortcuts import render
from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(is_active=True)
    template_name = "products/product_list_page.html"
    context_object_name = "products"


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail_page.html"
