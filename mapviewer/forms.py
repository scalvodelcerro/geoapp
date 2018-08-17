from django.contrib.gis import forms
from django.utils.translation import ugettext_lazy
from .models import Yacimiento, Provincia, Municipio

class YacimientoForm(forms.ModelForm):
    class Meta:
        model = Yacimiento
        fields = ('nombre', 'localizacion', 'comunidad_autonoma', 'provincia', 'municipio', 'tipo', 'fase_historica', 'observaciones')
        labels = {
            'nombre' : ugettext_lazy('Nombre'),
            'localizacion' : ugettext_lazy('Localización'),
            'comunidad_autonoma' : ugettext_lazy('Comunidad autónoma'),
            'provincia' : ugettext_lazy('Provincia'),
            'municipio' : ugettext_lazy('Municipio'),
            'tipo' : ugettext_lazy('Tipo de yacimiento'),
            'fase_historica' : ugettext_lazy('Fase histórica'),
            'observaciones' : ugettext_lazy('Observaciones'),
        }
        widgets = {
            'localizacion' : forms.OSMWidget(attrs={
                'default_lat' : 40.4378698,
                'default_lon' : -3.8196207,
                'default_zoom' : 5,
            }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance.pk:
            self.fields['provincia'].queryset = self.instance.comunidad_autonoma.provincia_set.order_by('nombre')
            self.fields['municipio'].queryset = self.instance.provincia.municipio_set.order_by('nombre')
        else:
            self.fields['provincia'].queryset = Provincia.objects.none()
            self.fields['municipio'].queryset = Municipio.objects.none()
            if 'comunidad_autonoma' in self.data:
                try:
                    comunidad_autonoma_id = int(self.data.get('comunidad_autonoma'))
                    self.fields['provincia'].queryset = Provincia.objects.filter(comunidad_autonoma_id=comunidad_autonoma_id).order_by('nombre')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty
            if 'provincia' in self.data:
                try:
                    provincia_id = int(self.data.get('provincia'))
                    self.fields['municipio'].queryset = Municipio.objects.filter(provincia_id=provincia_id).order_by('nombre')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty
            
        
