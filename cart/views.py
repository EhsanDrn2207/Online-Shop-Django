from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .cart import Cart
from .forms import AddToCartForm
from products.models import Product


def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['product_update_quantity_form'] = AddToCartForm(
            initial={
                'quantity': item['quantity'],
                'inplace': True,
            },
        )
    return render(request, template_name='cart/cart_detail.html', context={'cart': cart})


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = AddToCartForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product=product, quantity=quantity, replace_current_quantity=cleaned_data['inplace'])

    return redirect('product-list')


def remove_from_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


@require_POST
def clear_cart_view(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, _("All products successfully removed from your cart"))

    else:
        messages.warning(request, _("Your cart is already empty"))

    return redirect('product-list')