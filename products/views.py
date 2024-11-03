from django.shortcuts import render
from django.views import generic

from .models import Product
from .forms import ProductForm


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(is_active=True)
    template_name = "products/product_list_page.html"
    context_object_name = "products"


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail_page.html"


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_create_page.html"


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_update_page.html"