from django.shortcuts import redirect
from . import models
from Menu.models import Product



def handle_cart_products(cart, product):
    if not models.CartProduct.objects.filter(product=product).exists():
        models.CartProduct.objects.create(
            cart=cart,
            product=product,
            qty=1
        ).save()
        return True


def cart_handler(request):
    
    if request.GET.get("add-to-cart"): # to check whether the user had pressed the add to cart button
        session = request.session.session_key
        product_id = request.GET.get("productId")
        product_to_be_added = Product.objects.get(id=int(product_id))
        if models.Cart.objects.filter(session=str(session)).exists(): # to check if  there's a cart with the current session then get the cart and edit its products  else create a new cart
            handle_cart_products(cart=models.Cart.objects.get(session=session), product=product_to_be_added)
            
        else:
            # if theres no cart with the current session. Creates new cart object
            created_cart = models.Cart.objects.create(              
                session=session
            ) 
            handle_cart_products(cart=created_cart, product=product_to_be_added)
            created_cart.save() 
            
    return redirect("/#menu")