from decimal import Decimal

from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
import json

# Create your views here.
from django.utils import timezone
from django.views.generic import ListView, DetailView

from ShoppingCartApp.models import Product, Cart, CartItem


class ProductListView(ListView):
    model = Product
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = CartItem.objects.all()
        quantity = CartItem.objects.aggregate(Sum('quantity'))
        context['quantity'] = quantity
        total_cart_price = Decimal('0.0')
        for item in CartItem.objects.all():
            product_price = item.product.price * item.quantity
            print(product_price)
            total_cart_price += product_price
            print(total_cart_price)
        context['total_price'] = total_cart_price
        return context


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product ID:', product_id)
    # # Create a new CartItem
    product = Product.objects.get(id=product_id)
    print('ProductObj:', product)
    cart, created = Cart.objects.get_or_create()
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if action == 'add':
        cart_item.quantity = (cart_item.quantity + 1)
    elif action == 'remove':
        cart_item.quantity = (cart_item.quantity - 1)
    cart_item.save()
    if cart_item.quantity <= 0:
        cart_item.delete()
    return JsonResponse('Item was added', safe=False)


def get_cart(request):
    return render(request, 'ShoppingCartApp/cart.html', {'cart': Cart(request)})
