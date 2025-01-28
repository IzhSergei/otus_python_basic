import pytest
from    django.urls import reverse
from shop_app.models import Product



# Create your tests here.
def test_shop_start(client):
    url = reverse('shop_start')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Добро пожаловать' in response.content.decode('utf-8')


@pytest.mark.django_db
def test_category_list(client):
    url = reverse('category_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'добавить категорию' in response.content.decode('utf-8')
    assert 'Категории' in response.content.decode('utf-8')

@pytest.mark.django_db
def test_products_list(client):
    url = reverse('products_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'добавить товар' in response.content.decode('utf-8')
    assert 'Товары' in response.content.decode('utf-8')



@pytest.mark.django_db
def test_product_detail(client, category, product):
    url = reverse('products_detail')
    response=client.get(url)

    assert response.status_code == 200

    # created_product = Product.objects.last()
    # assert created_product.name == 'Тестовый товар'
    # assert created_product.description == 'Тестовое описание товара'
    # assert created_product.price == 1000
    # assert created_product.category.id == 1