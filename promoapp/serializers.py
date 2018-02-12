from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

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


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','pais','ciudad','foto','direccion','password','favoritas')
        read_only_fields = ('is_superuser', 'is_staff', 'groups',
                            'user_permissions', 'last_login', 'date_joined', 'is_active')
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        now = timezone.now()

        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            pais=validated_data['pais'],
            ciudad=validated_data['ciudad'],
            foto=validated_data['foto'],
            direccion=validated_data['direccion'],
            date_joined=now,
            is_active=True,
            is_superuser=True,
            is_staff=True
        )

        user.set_password(validated_data['password'])
        user.save()
        return user