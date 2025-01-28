import pytest
from django.urls import reverse
from shop_app.models import Category, Product
from shop_app.forms import ProductModelForm, CategoryForm


@pytest.mark.django_db
def test_product_create_view(mocker, client):
    # Создаем тестовую
    Category.objects.create(name="Тестовая категория", description='Тестовое описание категории')

    # Мокаем метод save() на уровне экземпляра модели
    mock_save = mocker.patch('shop_app.models.Product.save', autospec=True)


    url = reverse('add_product')
    response=client.post(url, data={
    'name':"Тестовый товар",
    'description':'Тестовое описание товара',
    'price':'1000',
    'category': '1'
    })

    # Проверяем, что save() был вызван
    assert mock_save.call_count == 1, "Метод save() должен быть вызван один раз."

    # Проверяем, что запрос завершился редиректом
    assert response.status_code == 302, "Запрос должен завершиться перенаправлением."

    # Дополнительно можно проверить, что объект создан с правильными данными
    # created_product = Product.objects.last()
    # assert created_product.name == 'Тестовый товар'
    # assert created_product.description == 'Тестовое описание товара'
    # assert created_product.price == 1000
    # assert created_product.category.id == 1

