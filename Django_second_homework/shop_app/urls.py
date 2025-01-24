from django.urls import path

from . import views

urlpatterns = [
    path("", views.shop_start, name="shop_start"),
    path("category/", views.category_list, name="category_list"),
    path("product/", views.products_list, name="products_list"),
    path(
        "category/<int:category_id>/", views.category_include, name="category_include"
    ),
    path("product/<int:product_id>/", views.products_detail, name="products_detail"),
    path("category/add_category/", views.add_category, name="add_category"),
    path("product/add_product/", views.add_product, name="add_product"),
    path(
        "product/edit_product/<int:product_id>/",
        views.edit_product,
        name="edit_product",
    ),
]
