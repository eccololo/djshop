from django.shortcuts import render
from .models import Category, Product


def shop(request):

    all_products = Product.objects.all()
    context = {
        "my_products": all_products
    }

    return render(request, template_name="shop/shop.html", context=context)


def categories(request):

    all_categories = Category.objects.all()

    return {"all_categories": all_categories}
