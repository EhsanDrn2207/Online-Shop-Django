from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Product, Comment
from .forms import ProductForm, CommentForm


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(is_active=True)
    template_name = "products/product_list_page.html"
    context_object_name = "products"


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_create_page.html"


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_update_page.html"


class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = "products/product_delete_page.html"
    success_url = reverse_lazy("product-list")


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, pk=product_id)
        obj.product = product
        return super().form_valid(form)

