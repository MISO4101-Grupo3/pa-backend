from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


## App

# Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        # fields= ('id','nombre',)
        fields = '__all__'
        read_only_fields = ('id',)


# Ciudad
class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        # fields= ('id', 'nombre',)
        fields = '__all__'
        read_only_fields = ('id',)


# Promocion
class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        # fields= ('id','nombre','descripcion','comentarios',)
        fields = '__all__'
        read_only_fields = ('id',)


# Comentario
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        # fields= ('id','texto','correo','promocion')
        fields = '__all__'

        read_only_fields = ('id',)
