from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    email_id = models.EmailField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    details = models.CharField(max_length=400, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Specs(models.Model):
    name = models.CharField(max_length=300, null=True)
    value = models.CharField(max_length=300, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Orders(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.OneToOneField(Customer, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='PENDING')
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def save(self, *args, **kwargs):
        self.total = self.get_total_cost()
        super(Orders, self).save(*args, **kwargs)


class ProductOrder(models.Model):
    """ Adding order model"""
    order = models.ForeignKey(Orders, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.product.price * self.quantity

    def save(self, *args, **kwargs):
        self.order.save()
        super(ProductOrder, self).save(*args, **kwargs)

    #
