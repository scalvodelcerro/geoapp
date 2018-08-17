from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class ComunidadAutonoma(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    comunidad_autonoma = models.ForeignKey(ComunidadAutonoma, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nombre
    
class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nombre
    
class TipoYacimiento(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class TipoFaseHistorica(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Yacimiento(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    localizacion = gis_models.PolygonField()
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
    comunidad_autonoma = models.ForeignKey(ComunidadAutonoma, on_delete=models.SET_NULL, null=True)
    tipo = models.ForeignKey(TipoYacimiento, on_delete=models.SET_NULL, null=True)
    fase_historica = models.ForeignKey(TipoFaseHistorica, on_delete=models.SET_NULL, null=True)
    #cronologia
    #intervenciones
    #bibliografia
    observaciones = models.TextField()
    
    def __str__(self):
        return self.nombre
    