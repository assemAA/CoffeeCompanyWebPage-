from django.db import models

# Create your models here.

class Review(models.Model):
    review_text = models.TextField(max_length=150, verbose_name="Review&Comment Text")
    related_name = models.CharField(max_length=50, verbose_name="Customer Name")
    
    class Meta:
        verbose_name= "Reviews"
        verbose_name_plural= "Reviews"
        
    def __str__(self):
        return f"{self.customer_name}"
    
   