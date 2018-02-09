from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'ciudades', CiudadViewSet)
router.register(r'promociones', PromocionViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/login', user_login),
    url(r'auth/me',user_whoami),
]

urlpatterns += router.urls
