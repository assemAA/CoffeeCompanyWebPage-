from django.shortcuts import redirect
from . import models
from Shopping_Cart.models import Cart
# Create your views here.

def orders_handler(request):
    if request.method == "POST":
        session = request.session.session_key
        customer_cart = Cart.objects.get(session=session)
        models.Order.objects.create(
            related_customer_name = request.POST.get("customer_name"),
            address = request.POST.get("customer_address"),
            phone_number = request.POST.get("customer_number"),
            related_cart = customer_cart

        ).save()
    
    return redirect("/")