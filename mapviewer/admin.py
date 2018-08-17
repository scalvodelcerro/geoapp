from django.contrib.gis import admin
from .models import Yacimiento

# Register your models here.
admin.site.register(Yacimiento, admin.GeoModelAdmin)