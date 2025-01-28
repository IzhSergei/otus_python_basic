import pytest
from    django.urls import reverse
from shop_app.models import Product


@pytest.mark.django_db
def test_product_add(client, category):
    url = reverse('add_product')
    response=client.post(url, data={
    'name':"Тестовый товар",
    'description':'Тестовое описание товара',
    'price':'1000',
    'category': '1'
    })

    assert response.status_code == 302

    created_product = Product.objects.last()
    assert created_product.name == 'Тестовый товар'
    assert created_product.description == 'Тестовое описание товара'
    assert created_product.price == 1000
    assert created_product.category.id == 1

