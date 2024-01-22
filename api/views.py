
from rest_framework import generics
from .models import Shoes, Sweater, Jacket, Pants  # Asegúrate de importar tu modelo
from .serializers import ShoesSerializer, SweaterSerializer, JacketSerializer, PantsSerializer  # Asegúrate de importar tu serializador
from django.http import HttpResponse

class ShoesList(generics.ListAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer

class SweaterList(generics.ListAPIView):
    queryset = Sweater.objects.all()
    serializer_class = SweaterSerializer

class JacketList(generics.ListAPIView):
    queryset = Jacket.objects.all()
    serializer_class = JacketSerializer

class PantsList(generics.ListAPIView):
    queryset = Pants.objects.all()
    serializer_class = PantsSerializer
