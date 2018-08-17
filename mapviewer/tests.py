from django.test import TestCase
from unittest.mock import patch
from django.contrib.gis.geos import Polygon
from mapviewer.models import ComunidadAutonoma, Provincia, Municipio,\
    TipoYacimiento, TipoFaseHistorica, Yacimiento
from django.urls.base import reverse
from django.contrib.auth.models import User

# Create your tests here.

#Models tests
class ComunidadAutonomaTest(TestCase):
    
    def test_str_debe_devolver_nombre(self):
        w = ComunidadAutonoma(nombre="Nombre")
        self.assertEqual(w.__str__(), w.nombre)
        
class ProvinciaTest(TestCase):
    
    def test_str_debe_devolver_nombre(self):
        w = Provincia(nombre="Nombre")
        self.assertEqual(w.__str__(), w.nombre)
        
class MunicipioTest(TestCase):
    
    def test_str_debe_devolver_nombre(self):
        w = Municipio(nombre="Nombre")
        self.assertEqual(w.__str__(), w.nombre)
        
class TipoYacimientoTest(TestCase):
    
    def test_str_debe_devolver_nombre(self):
        w = TipoYacimiento(nombre="Nombre")
        self.assertEqual(w.__str__(), w.nombre)
        
class TipoFaseHistoricaTest(TestCase):
    
    def test_str_debe_devolver_nombre(self):
        w = TipoFaseHistorica(nombre="Nombre")
        self.assertEqual(w.__str__(), w.nombre)
        
class YacimientoTest(TestCase):
    
    def test_str_debe_devolver_nombre(self):
        w = Yacimiento(nombre="Nombre")
        self.assertEqual(w.__str__(), w.nombre)
        
#Views tests
class ListadoYacimientosTest(TestCase):
    
    def test_lista_vacia_si_no_hay_yacimientos(self):
        with patch.object(Yacimiento.objects, 'all', return_value=[]):   
            url = reverse('listado_yacimientos')
            resp = self.client.get(url)
            
            self.assertEqual(resp.status_code, 200)
            self.assertTemplateUsed(resp, 'mapviewer/listado_yacimientos.html')
        
    def test_yacimientos_en_lista(self):
        nombre_y1 = "Nombre Y1"
        nombre_y2 = "Nombre Y2"
        y1 = Yacimiento(pk=1, nombre=nombre_y1)
        y2 = Yacimiento(pk=2, nombre=nombre_y2)
#         m_yacimiento_model.objects.all.return_value = [y1]        
        with patch.object(Yacimiento.objects, 'all', return_value=[y1, y2]):        
            url = reverse('listado_yacimientos')
            resp = self.client.get(url) 
            
            self.assertEqual(resp.status_code, 200)
            self.assertTemplateUsed(resp, 'mapviewer/listado_yacimientos.html')
            self.assertIn(y1.nombre.encode(), resp.content)
            self.assertIn(y2.nombre.encode(), resp.content)
        
class DetalleYacimientoTest(TestCase):
    def test_no_existe_yacimiento(self):
        with patch.object(Yacimiento.objects, 'all', return_value=Yacimiento.objects.none()):
            url = reverse('detalle_yacimiento', args=[1])
            resp = self.client.get(url)
            
            self.assertEqual(resp.status_code, 404)
            self.assertTemplateNotUsed(resp, 'mapviewer/detalle_yacimiento.html')
            
