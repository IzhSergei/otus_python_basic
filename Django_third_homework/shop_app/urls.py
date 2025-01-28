from django.urls import path

from . import views

urlpatterns = [
    path("", views.shop_start, name="shop_start"),
    path("category/", views.CategoryListView.as_view(), name="category_list"),
    path("product/", views.ProductListView.as_view(), name="products_list"),
    path(
        "category/<int:category_id>/", views.CategoryIncListView.as_view(), name="category_include"
    ),
    path("product/<int:product_id>/", views.ProductDetailView.as_view(), name="products_detail"),
    path("category/add_category/", views.CategoryAddView.as_view(), name="add_category"),
    path("product/add_product/", views.ProductAddView.as_view(), name="add_product"),
    path(
        "product/<int:product_id>/edit_product/",
        views.ProductUpdateView.as_view(),
        name="edit_product",
    ),
    path("product/<int:product_id>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("category/<int:category_id>/delete/", views.CategoryDeleteView.as_view(), name="category_delete"),

]
