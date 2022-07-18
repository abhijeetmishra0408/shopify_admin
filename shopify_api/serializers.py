from rest_framework import serializers
from .models import Orders, Products, ProductsVariant


class BestProductSerializer(serializers.Serializer):
    class Meta:
        model = Orders
        field = ["total_price", "product_name"]
        product_name = serializers.SerializerMethodField("get_product_name")

        def get_product_name(self, obj):
            return obj.product.name
