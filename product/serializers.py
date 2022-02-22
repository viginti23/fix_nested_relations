from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import Category, Product, Variant, Topping, ProductVariant


class SauceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = (
            "id",
            "name",
            "price"
        )


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = (
            "id",
            "name",
            "price"
        )


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = (
            "id",
            "size",
            "description"
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
        )


class ProductSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail",
            "category"
        )


class ProductVariantSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    product = ProductSerializer()
    variant = VariantSerializer()

    class Meta:
        model = ProductVariant
        fields = (
            "id",
            "product",
            "variant",
            "is_default",
            "price"
        )


