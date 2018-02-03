from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


## App

# Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields= ('id','nombre',)
        read_only_fields= ('id',)

# Ciudad
class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields= ('id', 'nombre',)
        read_only_fields= ('id',)


# Comentario
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields= ('id','texto','correo','promocion')
        read_only_fields= ()

# Promocion
class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        fields= ('id','nombre','descripcion','comentarios',)
        read_only_fields= ('comentarios',)
    
