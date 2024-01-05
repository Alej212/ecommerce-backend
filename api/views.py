
from rest_framework import generics
from .models import Shoes  # Asegúrate de importar tu modelo
from .serializers import ShoeSerializer  # Asegúrate de importar tu serializador

class ShoesList(generics.ListAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoeSerializer