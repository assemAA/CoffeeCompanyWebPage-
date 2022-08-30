from django.shortcuts import render
from Menu.models import Product 
from Shopping_Cart.models import Cart, CartProduct

def home_page(request):
     products = Product.objects.all()
     if not request.session.exists(request.session.session_key):
          request.session.create()
     session = request.session.session_key
     cart = Cart.objects.get_or_create(session=session)
     cart_products = CartProduct.objects.filter(cart = cart[0].id)
     return render(request, "index.html", {"products": products, "cart_products":cart_products})