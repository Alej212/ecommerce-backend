from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Shoes, Sweaters, Jackets, Pants
from .serializers import ShoesSerializer, SweatersSerializer, JacketsSerializer, PantsSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from bson import ObjectId
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


class ShoesList(generics.ListAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer

class SweaterList(generics.ListAPIView):
    queryset = Sweaters.objects.all()
    serializer_class = SweatersSerializer

class JacketList(generics.ListAPIView):
    queryset = Jackets.objects.all()
    serializer_class = JacketsSerializer

class PantsList(generics.ListAPIView):
    queryset = Pants.objects.all()
    serializer_class = PantsSerializer
    
class ShoesDetail(APIView):
    def get(self, request, custom_id):
        try:
            shoes = Shoes.objects.get(custom_id=custom_id)
        except Shoes.DoesNotExist:
            raise NotFound(detail="No se encontró un objeto Shoes con el id proporcionado.")
        data = ShoesSerializer(shoes).data
        return Response(data)


class SweatersDetail(APIView):
    def get(self, request, custom_id):
        try:
            sweater = Sweaters.objects.get(custom_id=custom_id)  # Aquí es donde consultas la base de datos
        except Sweaters.DoesNotExist:
            raise NotFound(detail="No se encontró un objeto Sweater con el id proporcionado.")
        data = SweatersSerializer(sweater).data
        return Response(data)

class JacketsDetail(APIView):
    def get(self, request, custom_id):
        try:
            shoes = Jackets.objects.get(custom_id=custom_id)
        except Jackets.DoesNotExist:
            raise NotFound(detail="No se encontró un objeto Shoes con el id proporcionado.")
        data = JacketsSerializer(shoes).data
        return Response(data)


class PantsDetail(APIView):
    def get(self, request, custom_id):
        try:
            sweater = Pants.objects.get(custom_id=custom_id)  # Aquí es donde consultas la base de datos
        except Pants.DoesNotExist:
            raise NotFound(detail="No se encontró un objeto Sweater con el id proporcionado.")
        data = PantsSerializer(sweater).data
        return Response(data)
