from django.db import models
from Menu.models import Product


# Create your models here.
class Cart(models.Model):
    session = models.CharField(max_length=350, verbose_name="Session") #session id for the current anonymous user
    total_price = models.FloatField(verbose_name="Total price", null=True, blank=True)
    
    
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(verbose_name="QTY")
    
    