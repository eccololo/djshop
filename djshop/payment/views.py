from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

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

    # Clear the shopping cart

    for key in list(request.session.keys()):

        if key == "session_key":

            del request.session[key]

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

        product_list = []

        if request.user.is_authenticated:

            order = Order.objects.create(
                full_name=name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=total_cost,
                user=request.user
            )


            for item in cart:

                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    quantity=item["qty"],
                    price=item["price"],
                    user=request.user
                )

                product_list.append(item["product"])
        
        else:

            order = Order.objects.create(
                full_name=name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=total_cost,
            )

            for item in cart:

                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    quantity=item["qty"],
                    price=item["price"],
                )

                product_list.append(item["product"])

        order_success = True

        title = "Your order is received!"
        message = f"""
        Hi,

        We have received you order. 
        You can below list of your purchases: \n
        {str(product_list)}
        \n
        Total cost: ${str(cart.get_total())}
        \n
        Thank you for your purchase!
        """
        sender = settings.EMAIL_HOST_USER

        send_mail(title, message, sender, [email], fail_silently=False)

        return JsonResponse({"success": order_success})


def test_email(request):
    send_mail(
        'Test email',
        'If you see this, it works.',
        settings.EMAIL_HOST_USER,
        ['mateusz.hyla.it@gmail.com'],
        fail_silently=False
    )
    return JsonResponse({"status": "sent"})