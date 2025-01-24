from decimal import Decimal
from django.contrib import admin
from .models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    ordering = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "category", "created_at")
    ordering = ("name",)
    search_fields = ("name",)
    list_filter = ("category",)
    search_help_text = "Введите наименование товара"
    readonly_fields = ("created_at",)

    @admin.action(description="Сделать скидку 10 процентов")
    def reduce_price(self, request, queryset):
        for product in queryset:
            product.price -= Decimal(float(product.price) * 0.1)
            product.save()
        self.message_user(request, f"цена у {queryset.count()} уменьшена на 10%")

    actions = [reduce_price]
