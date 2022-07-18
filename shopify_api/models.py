# from itertools import product
# from locale import currency
# from pyexpat import model
# from statistics import mode
from django.db import models

# from requests import delete

# Create your models here.
class Products(models.Model):
    shopify_product_id = models.DecimalField(
        max_digits=16, decimal_places=0, unique=True
    )
    name = models.CharField(max_length=255, null=True)
    body_html = models.TextField(null=True)
    status = models.CharField(max_length=20, null=True)
    handle = models.CharField(max_length=255, null=True)
    image = models.URLField(null=True)


class ProductsVariant(models.Model):
    product = models.ForeignKey("Products", on_delete=models.CASCADE, null=True)
    shopify_product_id = models.DecimalField(max_digits=16, decimal_places=0)
    shopify_Variant_id = models.DecimalField(
        max_digits=18, decimal_places=0, unique=True
    )
    price = models.DecimalField(max_digits=7, decimal_places=2)
    sku = models.CharField(max_length=255, null=True)


class Orders(models.Model):
    shopify_order_id = models.DecimalField(max_digits=16, decimal_places=0)
    currency = models.CharField(max_length=25, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=20, null=True)
    product = models.ForeignKey("Products", on_delete=models.CASCADE, null=True)
    productvariant = models.ForeignKey(
        "ProductsVariant", on_delete=models.CASCADE, null=True
    )
    order_date = models.DateTimeField(null=False)
