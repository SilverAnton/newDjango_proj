from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "product.html", context)


def category(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, "category.html", context)


def base(request):
    context = {
        'base_templates': 'base'
    }
    return render(request, 'base.html', context)


def product_review(request, pk):
    product_ = get_object_or_404(Product, pk=pk)
    context = {'product': product_}
    return render(request, "product_review.html", context)


def category_review(request):
    context = {'category_review': 'category_review'}
    return render(request, "category_review.html", context)



