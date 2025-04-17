from django.shortcuts import render

from .models import ShippingAddress


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