from rest_framework import serializers

from product.models import Topping, Sauce, ProductVariant
from product.serializers import ProductVariantSerializer, ToppingSerializer, SauceSerializer
from .models import Order, OrderItem
from drf_writable_nested.serializers import WritableNestedModelSerializer


class MyOrderItemSerializer(WritableNestedModelSerializer):
    product_variant = ProductVariantSerializer()
    toppings = ToppingSerializer(many=True)

    class Meta:
        model = OrderItem
        fields = (
            "product_variant",
            "toppings",
            "sauces",
            "total_price",
            "quantity"
        )


class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "postcode",
            "place",
            "phone",
            "items",
            "created_at",
            "paid_amount",
        )


class OrderItemSerializer(WritableNestedModelSerializer):
    sauces = serializers.PrimaryKeyRelatedField(read_only=True)
    toppings = serializers.PrimaryKeyRelatedField(read_only=True)
    product_variant = ProductVariantSerializer()
    class Meta:
        model = OrderItem
        fields = (
            "product_variant",
            "sauces",
            "toppings",
            "total_price",
            "quantity",
        )


class OrderSerializer(WritableNestedModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Order
        fields = (
            "id",
            'user',
            "first_name",
            "last_name",
            "email",
            "address",
            "postcode",
            "place",
            "phone",
            "items"
        )
