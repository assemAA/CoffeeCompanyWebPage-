from django.db import models
from Shopping_Cart.models import Cart


# Create your models here.

class Order(models.Model):
    related_customer_name = models.CharField(max_length=100, verbose_name="Customer Name")
    address = models.TextField(verbose_name="Address")
    phone_number = models.CharField(max_length=350,verbose_name="Phone Number")
    related_cart = models.ForeignKey(Cart,on_delete=models.CASCADE, verbose_name="Related cart", null=True, blank=True)
    
    class Meta:
        verbose_name= "Order"
        verbose_name_plural= "Orders"
    
    def __str__(self):
        return f"{self.related_customer_name}"