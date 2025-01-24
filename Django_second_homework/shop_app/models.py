from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="product"
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
