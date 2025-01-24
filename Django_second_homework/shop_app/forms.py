from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class CategoryForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Наименование",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите наименование категории",
            }
        ),
    )
    description = forms.CharField(
        max_length=200,
        label="Описание",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Введите описание продукта",
            }
        ),
    )


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category"]
        labels = {
            "name": "Наименование",
            "description": "Описание",
            "price": "Цена",
            "category": "Категория",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите наименование товара",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Введите описание товара",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите стоимость товара",
                }
            ),
            # "category": forms.CheckboxSelectMultiple(),
        }

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0.1:
            raise forms.ValidationError("Цена должна быть не менее 0,1")
        return price

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get("description")
        forbidden_words = ["бесплатно", "перепрошит", "разбит"]
        if content:
            for word in forbidden_words:
                if word in content.lower():
                    raise ValidationError(f"Содержит запрещенное слово: {word}")
