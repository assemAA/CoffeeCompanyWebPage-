from django.db import models
from django.db.models.fields import related

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="Category Name")
    
    class Meta:
        verbose_name= "Category"
        verbose_name_plural= "Categories"
        
    def __str__(self):
        return f"{self.category_name}"
    
class Product(models.Model):
    product_image = models.ImageField(verbose_name="Product Image")
    product_name = models.CharField(max_length=100, verbose_name="Product Name")
    related_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Related Category")
    product_price = models.IntegerField(verbose_name="Product Price")
    on_sale = models.BooleanField(default=False , verbose_name="on sale")
    price_sale = models.IntegerField(verbose_name="Price Sale")
    
    class Meta:
        verbose_name= "Product"
        verbose_name_plural= "Products"
    
    def __str__(self):
        return f"{self.product_name}"