from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    digital = models.BooleanField(default=False,  null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photo_1 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except Exception as e:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        User,  on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def totalPrice(self):

        return sum([item.totalPrice for item in self.orderitem_set.all()])

    @property
    def totalItem(self):
        return sum([item.quantity for item in self.orderitem_set.all()])

    @property
    def shipping(self):
        all_items = self.orderitem_set.all()
        result = False
        for item in all_items:
            result = False
            if item.product.digital == False:
                result = True
        return result


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def totalPrice(self):
        total = self.product.price*self.quantity
        return total


class ShippingAdress(models.Model):
    customer = models.ForeignKey(
        User,  on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order,  on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
