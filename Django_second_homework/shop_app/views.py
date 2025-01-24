from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

# from django.http import HttpResponse
# from django.template.defaultfilters import title

from .forms import CategoryForm, ProductModelForm
from .models import Product, Category

# Create your views here.


def shop_start(request):
    return render(request, "shop_app/shop_start.html")


def category_list(request):
    categories = Category.objects.all().values("id", "name")
    context = {"title": "категории", "categories": categories}
    return render(request, "shop_app/category_list.html", context=context)


def products_list(request):
    products = Product.objects.all().values("id", "name", "description", "price")
    context = {"title": "товары", "products": products}
    return render(request, "shop_app/products_list.html", context=context)


def category_include(request, category_id):
    category_des = get_object_or_404(Category, id=category_id).description
    # category_inc = get_list_or_404(Product, category=category_id)
    category_inc = Product.objects.filter(category=category_id).values("id", "name")
    context = {"title": category_des, "products": category_inc}
    return render(request, "shop_app/category_include.html", context=context)


def products_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        "title": product.category.description,
        "category": product.category.id,
        "products": product,
    }
    return render(request, "shop_app/products_detail.html", context=context)


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            category = Category(name=name, description=description)
            category.save()
            return redirect("category_list")
    else:
        form = CategoryForm()
    context = {"title": "добавление категории", "form": form}
    return render(request, "shop_app/add_category.html", context=context)


def add_product(request):
    if request.method == "POST":
        form = ProductModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            price = form.cleaned_data["price"]
            category = form.cleaned_data["category"]

            product = Product(
                name=name, description=description, price=price, category=category
            )
            product.save()
            return redirect("products_list")
        else:
            print(form.errors)
    else:
        form = ProductModelForm()
    context = {"title": "Добавление товара", "form": form}
    return render(request, "shop_app/add_product.html", context=context)


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products_list")
        else:
            print(form.errors)
    else:
        form = ProductModelForm(instance=product)
    context = {"title": "Редактирование карточки товара", "form": form}
    return render(request, "shop_app/edit_product.html", context=context)
