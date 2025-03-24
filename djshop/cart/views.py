from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .cart import Cart
from shop.models import Product


def cart_summary(request):

    cart = Cart(request)

    context = {
        "cart": cart
    }

    return render(request, "cart/cart-summary.html", context=context)


def cart_update(request):

    pass


def cart_delete(request):

    pass


def cart_add(request):

    cart = Cart(request)
    
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity"))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, product_qty=product_quantity)
        
        cart_quantity = cart.__len__()

        response = JsonResponse({
            "qty": cart_quantity
        })

        return response
        
