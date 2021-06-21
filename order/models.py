from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm

from product.models import Product


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    @property
    def amount(self):
        return (self.quantity * self.product.price)

    @property
    def price(self):
        return (self.product.price)


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']


class Order(models.Model):
    STATUS= (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnTable', 'OnTable'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5)
    tableno = models.CharField(max_length=20, blank=True)
    total = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=15, default='New', choices=STATUS)
    ip = models.CharField(max_length=20, blank=True)
    adminnote = models.CharField(max_length=100, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['tableno']


class OrderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    total = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=15, default='New', choices=STATUS)
    ip = models.CharField(max_length=20, blank=True)
    adminnote = models.CharField(max_length=100, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title