from django.contrib import admin

# Register your models here.
from ShoppingCartApp.models import Cart, Product, CartItem

admin.site.register(Product)
admin.site.register(CartItem)


class CartItemInline(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]


admin.site.register(Cart, CartAdmin)
