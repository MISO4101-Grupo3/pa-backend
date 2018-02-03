from django.shortcuts import render

from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from .serializers import *
from .models import *

def index(request):
    return render(request, 'index.html')

# App


# Categoria
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('-id')
    serializer_class = CategoriaSerializer


# Ciudad
class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all().order_by('-id')
    serializer_class = CiudadSerializer


# Comentario
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all().order_by('-id')
    serializer_class = ComentarioSerializer


# Promocion
class PromocionViewSet(viewsets.ModelViewSet):
    queryset = Promocion.objects.all().order_by('-id')
    serializer_class = PromocionSerializer

