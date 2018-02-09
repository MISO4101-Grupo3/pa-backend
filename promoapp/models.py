from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _

from promoapp.utils import *


class UserManager(UserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = email.lower();
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    class Meta:
        verbose_name_plural = "Usuarios"

    username = None
    email = models.EmailField(_('correo'), unique=True)
    foto = models.ImageField(null=True, blank=True, upload_to=UploadToPathAndRename('uploads/'))
    direccion = models.CharField(null=True, blank=True, max_length=255)
    pais = models.CharField(null=False, blank=False, max_length=100)
    favoritas = models.ManyToManyField('Categoria', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


# Categoria
class Categoria(models.Model):
    def __str__(self):
        return self.nombre

    nombre = models.CharField(null=False, blank=False, unique=True, max_length=50)


# Ciudad
class Ciudad(models.Model):
    class Meta:
        verbose_name_plural = "ciudades"

    def __str__(self):
        return str(self.nombre)

    nombre = models.CharField(null=False, blank=False, unique=True, max_length=60)


# Promocion
class Promocion(models.Model):
    class Meta:
        verbose_name_plural = "promociones"

    def __str__(self):
        return self.nombre + " (" + str(self.id) + ")"

    nombre = models.CharField(null=False, blank=False, max_length=250)
    descripcion = models.TextField(null=False, blank=False)
    imagen = models.ImageField(null=True, blank=True, upload_to=UploadToPathAndRename('uploads/'))
    precio = models.FloatField(null=False, blank=False)
    fechaInicio = models.DateField(null=False, blank=False)
    fechaFin = models.DateField(null=True, blank=True)
    resumen = models.TextField(null=False, blank=False)
    categoria = models.ForeignKey('Categoria', null=True, on_delete=models.CASCADE)
    ciudad = models.ForeignKey('Ciudad', null=True, on_delete=models.CASCADE)


# Comentario
class Comentario(models.Model):
    def __str__(self):
        return self.correo + ':' + str(self.id)

    texto = models.TextField(null=False, blank=False)
    correo = models.EmailField(null=False, blank=False)
    promocion = models.ForeignKey('Promocion', related_name='comentarios', null=True, on_delete=models.CASCADE)
