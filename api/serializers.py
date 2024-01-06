from rest_framework import serializers
from .models import Shoes

class ShoeSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = Shoes
        fields = ['img', 'title', 'money']

    def get_img(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.img.url)
        return obj.img.url
