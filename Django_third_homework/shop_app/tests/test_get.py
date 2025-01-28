import pytest
from django.urls import reverse
from shop_app.models import Product




@pytest.mark.django_db
def test_product_detail(client, category):
    product=Product.objects.create(name="Тестовый товар", description='Тестовое описание товара', price=10000, category=category)
    product=product.objects.values()
    print(product)
    url = reverse('products_detail')
    response=client.get(url, query_params=product)

    assert response.status_code == 200

    # created_product = Product.objects.last()
    # assert created_product.name == 'Тестовый товар'
    # assert created_product.description == 'Тестовое описание товара'
    # assert created_product.price == 1000
    # assert created_product.category.id == 1

    # , query_params = {"name": "fred", "age": 7}