from rest_framework import serializers
from .models import Products, Shoes, Sweater, Jacket, Pants

class ProductsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id')
    class Meta:
        model = Products
        fields = ['id','image', 'title', 'price', 'category', 'type_product']

class ShoesSerializer(ProductsSerializer):
    class Meta(ProductsSerializer.Meta):
        model = Shoes

class SweaterSerializer(ProductsSerializer):
    class Meta(ProductsSerializer.Meta):
        model = Sweater

class JacketSerializer(ProductsSerializer):
    class Meta(ProductsSerializer.Meta):
        model = Jacket

class PantsSerializer(ProductsSerializer):
    class Meta(ProductsSerializer.Meta):
        model = Pants