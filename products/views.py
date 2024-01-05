from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Shoe  # Asegúrate de importar tu modelo
from rest_framework import generics
from .serializers import ShoeSerializer
import logging

logger = logging.getLogger(__name__)

def check_connection(request):  # Agrega 'request' aquí
    try:
        # Intenta obtener un producto por su título
        product = Shoe.objects.get(title='Test Product')
        return HttpResponse('Conexión exitosa. Producto encontrado: ' + product.title)
    except ObjectDoesNotExist:
        return HttpResponse('No se encontró el producto. Pero la conexión fue exitosa.')
    except Exception as e:
        logger.error('Error al intentar conectar a la base de datos: ' + str(e))
        return HttpResponse('Error al intentar conectar a la base de datos.')

class ShoeList(generics.ListAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

from django.http import JsonResponse

def viewdata(request):
    data = list(Shoe.objects.values())
    print(data)
    return JsonResponse(data, safe=False)
