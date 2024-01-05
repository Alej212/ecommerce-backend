from rest_framework import serializers
from .models import Shoes

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes
        fields = ['img', 'title', 'money']
