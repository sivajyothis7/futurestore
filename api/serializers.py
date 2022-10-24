from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from owner.models import Categories,Products

class CategorySerializer(ModelSerializer):

    class Meta:
        model=Categories
        fields="__all__"

class ProductSerializer(ModelSerializer):
    product_name=serializers.CharField(read_only=True)

    class Meta:
        model=Products
        fields="__all__"

    def create(self, validated_data):
        category=self.context.get("category")
        return Products.objects.create(**validated_data,category=category)