from rest_framework import serializers
from .models import Products, Shoes, Sweaters, Jackets, Pants

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['custom_id','image', 'title', 'price', 'genre', 'type_product']

class ShoesSerializer(ProductsSerializer):
    class Meta(ProductsSerializer.Meta):
        model = Shoes

class SweatersSerializer(ProductsSerializer):
    class Meta(ProductsSerializer.Meta):
        model = Sweaters

class JacketsSerializer(ProductsSerializer):
    class Meta(ProductsSerializer.Meta):
        model = Jackets

class PantsSerializer(ProductsSerializer):
    class Meta(ProductsSerializer.Meta):
        model = Pants
        