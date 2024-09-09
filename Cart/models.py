from django.db import models
from Signup.models import AppUser
from Products.models import Product
from Commerce.settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractBaseUser


class Cart(AbstractBaseUser):
    owner = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    num_of_items = models.IntegerField(default=0, blank=True)
    total = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Carts"

    def __str__(self):
        return f"{self.owner} - {self.num_of_items} item(s) in cart"


class CartItem(AbstractBaseUser):
    cart = models.ManyToManyField(Cart)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, blank=True)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', 'added']
        verbose_name_plural = "Cart Items"

    def __str__(self):
        return f"{self.quantity} x {self.product_id.name}"
    
