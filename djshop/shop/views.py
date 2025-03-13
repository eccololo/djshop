from django.shortcuts import render


def shop(request):

    return render(request, template_name="shop/shop.html")
