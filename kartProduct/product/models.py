from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().using("mongodb")


class ProductItems(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # objects = ProductManager()

    class Meta:
        verbose_name_plural = "product_items"

    def __str__(self):
        return str(self.name)
