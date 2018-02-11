from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render

from django.shortcuts import render
from rest_framework import filters, permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

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


# Promocion
class PromocionViewSet(viewsets.ModelViewSet):
    queryset = Promocion.objects.all().order_by('-id')
    serializer_class = PromocionSerializer


# Comentario
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all().order_by('-id')
    serializer_class = ComentarioSerializer


# Usuario
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UsuarioSerializer


class RegistroUsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistroUsuarioSerializer


# Auth

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def user_login(request):
    if 'email' not in request.data or 'password' not in request.data:
        return HttpResponseBadRequest()
    user = authenticate(username=request.data["email"], password=request.data["password"])
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    else:
        return HttpResponseBadRequest()


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def user_whoami(request):
    serializer = UsuarioSerializer(request.user, many=False)
    return JsonResponse(serializer.data)
