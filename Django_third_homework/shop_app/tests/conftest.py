import pytest
from shop_app.models import Product, Category




@pytest.fixture
def category():
    test_category=Category.objects.create(name="Тестовая категория", description='Тестовое описание категории')
    return test_category


@pytest.fixture
def product():
    return Product.objects.create(name="Тестовый товар", description='Тестовое описание товара', price=10000, category=1)