import pytest
from shop_app.models import Category, Product


@pytest.mark.django_db
def test_models():
    test_category=Category.objects.create(name='Тестовая категория', description='Тестовое описание категории')
    test_product=Product.objects.create(name='Тестовый товар', description='Тестовое описание товара',price='1000',category=test_category)

    assert Category.objects.count() == 1
    assert Product.objects.count() == 1
    assert test_category.name == 'Тестовая категория'
    assert test_category.description == 'Тестовое описание категории'
    assert test_product.name == 'Тестовый товар'
    assert test_product.description == 'Тестовое описание товара'
    assert test_product.price == '1000'
    assert test_product.category.id == 1
    assert test_product.category.description == 'Тестовое описание категории'






