import pytest
from shop_app.models import Category
from shop_app.forms import ProductModelForm, CategoryForm


@pytest.mark.django_db
def test_category_form():
    form_data = {
        'name': 'Тестовая категория',
        'description': 'Тестовое описание категории',
    }

    form = CategoryForm(data=form_data)
    assert form.is_valid()

    cleaned_data = form.cleaned_data
    assert cleaned_data['name'] == form_data['name']
    assert cleaned_data['description'] == form_data['description']



@pytest.mark.django_db
def test_product_form():
    form_data = {
        'name': 'Тестовый товар',
        'description': 'Тестовое описание товара',
        'price': 100,
        'category': Category.objects.create(name="Тестовая категория", description='Тестовое описание категории')
    }

    form = ProductModelForm(data=form_data)
    assert form.is_valid()

    cleaned_data = form.cleaned_data
    assert cleaned_data['name'] == form_data['name']
    assert cleaned_data['description'] == form_data['description']
    assert cleaned_data['price'] == form_data['price']
    assert cleaned_data['category'] == form_data['category']

