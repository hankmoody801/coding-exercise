from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=True)
    image = models.ImageField(width_field=None, height_field=None)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", args=[str(self.id)])


class Cart(models.Model):
    creation_date = models.DateTimeField(default=datetime.now)
    complete = models.BooleanField(default=False, verbose_name=_('checked out'))

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    added_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.product.name
