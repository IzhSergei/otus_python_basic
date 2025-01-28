from django.contrib import messages

from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView,CreateView, UpdateView, DeleteView
from .forms import CategoryForm, ProductModelForm
from .models import Product, Category

# Create your views here.


def shop_start(request):
    return render(request, "shop_app/shop_start.html")


class CategoryListView(ListView):
    """Представление для вывода списка категорий"""

    template_name = "shop_app/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.values("id", "name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        return context



class ProductListView(ListView):
    """Представление для вывода списка товаров"""

    template_name = "shop_app/products_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.values("id", "name", "description", "price")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товары'
        return context



class CategoryIncListView(ListView):
    """Представление для вывода списка товаров в категории"""

    template_name = "shop_app/category_include.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['category_id']).values("id", "name")

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] =  get_object_or_404(Category, id=self.kwargs['category_id']).description
        context['category'] = self.kwargs['category_id']
        return context



class ProductDetailView(DetailView):
    """Представление для вывода детальной информации о товаре"""

    model = Product
    template_name = 'shop_app/products_detail.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'products'




class CategoryAddView(FormView):
    """Представление для добавления категории"""

    model = Category
    form_class = CategoryForm
    template_name = 'shop_app/add_category.html'
    success_url = reverse_lazy("category_list")
    extra_context = {"title":"добавление категории"}

    def form_valid(self, form):
        messages.success(self.request, 'категория успешно создана!')
        return super().form_valid(form)




class ProductAddView(CreateView):
    """Представление для добавления товара"""

    model = Product
    form_class = ProductModelForm
    template_name = 'shop_app/add_product.html'
    success_url = reverse_lazy("products_list")

    def form_valid(self, form):
        messages.success(self.request, 'продукт успешно добавлен!')
        return super().form_valid(form)



class ProductUpdateView(UpdateView):
    """Представление для редактирования карточки товара"""

    model = Product
    form_class = ProductModelForm
    template_name = 'shop_app/edit_product.html'
    success_url = reverse_lazy("products_list")
    pk_url_kwarg = 'product_id'
    extra_context = {"title":"Редактирование карточки товара"}

    def form_valid(self, form):
        messages.success(self.request, 'продукт успешно изменён!')
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    """Представление для удаления товара"""

    model = Product
    template_name = 'shop_app/product_delete.html'
    success_url = reverse_lazy("products_list")
    context_object_name = "product"
    pk_url_kwarg = 'product_id'
    extra_context =  {"title":"Удаление карточки товара"}


class CategoryDeleteView(DeleteView):
    """Представление для удаления категории"""

    model = Category
    template_name = 'shop_app/category_delete.html'
    success_url = reverse_lazy("category_list")
    context_object_name = "category"
    pk_url_kwarg = 'category_id'
    extra_context = {"title": "Удаление категории товаров"}
