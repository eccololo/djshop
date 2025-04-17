from django.shortcuts import render

from .models import ShippingAddress, Order, OrderItem

from cart.cart import Cart


def checkout(request):

    # Users with account - pre-fill form
    if request.user.is_authenticated:

        try:
            # Authenticated users with shipping info
            shipping_address = ShippingAddress.objects.get(user=request.user.id)

            context = {
                "shipping": shipping_address
            }

            return render(request, "payment/checkout.html", context)
        
        except:
            # Authenticated users with no shipping info
            return render(request, "payment/checkout.html")

    else:
        # Guest users
        return render(request, "payment/checkout.html")


def payment_success(request):

    return render(request, "payment/payment-success.html")


def payment_failed(request):

    return render(request, "payment/payment-failed.html")


def complete_order(request):

    if request.POST.get("action") == "post":

        name = request.POST.get("name")
        email = request.POST.get("email")

        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        city = request.POST.get("city")

        state = request.POST.get("state")
        zipcode = request.POST.get("zipcode")

        # All-in-one shipping address
        shipping_address = (address1 + "\n" + address2 + "\n" + 
                            city + "\n" + state + "\n" + zipcode)
        
        # Shopping cart information
        cart = Cart(request)

        # Get total cost of items
        total_cost = cart.get_total()

        
