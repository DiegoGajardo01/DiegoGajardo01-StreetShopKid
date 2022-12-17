from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='nombre')
    activo=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name_plural="Categoria"

class Producto(models.Model):
    codigo=models.CharField(max_length=10, primary_key=True)
    nombre=models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='nombre')
    imagen=models.CharField(max_length=250)
    marca=models.CharField(max_length=250)
    descripcion=models.TextField(blank=True, null=True)
    precio=models.IntegerField()
    cantidad=models.IntegerField(default=1)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    destacado=models.BooleanField(default=True)
    activo=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name_plural="Producto"
