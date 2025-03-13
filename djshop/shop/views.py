from django.shortcuts import render
from .models import Category


def shop(request):

    return render(request, template_name="shop/shop.html")


def categories(request):

    all_categories = Category.objects.all()

    return {"all_categories": all_categories}
