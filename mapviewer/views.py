from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Yacimiento, Provincia, Municipio
from .forms import YacimientoForm
from mapviewer.models import TipoYacimiento, TipoFaseHistorica

# Create your views here.

def listado_yacimientos(request):
    yacimientos = Yacimiento.objects.all()
    return render(request, 'mapviewer/listado_yacimientos.html', {'yacimientos' : yacimientos})

def detalle_yacimiento(request, pk):
    yacimiento = get_object_or_404(Yacimiento.objects.all(), pk=pk)
    return render(request, 'mapviewer/detalle_yacimiento.html', {'yacimiento' : yacimiento})

@login_required
def nuevo_yacimiento(request):
    if request.method == 'POST':
        form = YacimientoForm(request.POST)
        if form.is_valid():
            yacimiento = form.save(commit=False)
            yacimiento.usuario = request.user
            yacimiento.save()
            return redirect('detalle_yacimiento', pk=yacimiento.pk)
    else:
        form = YacimientoForm()
    return render(request, 'mapviewer/editar_yacimiento.html', {'form': form})

@login_required
def editar_yacimiento(request, pk):
    yacimiento = get_object_or_404(Yacimiento, pk=pk)
    if request.method == 'POST':
        form = YacimientoForm(request.POST, instance=yacimiento)
        if form.is_valid():
            yacimiento = form.save(commit=False)
            yacimiento.usuario = request.user
            yacimiento.save()
            return redirect('detalle_yacimiento', pk=yacimiento.pk)
    else:
        form = YacimientoForm(instance=yacimiento)
    return render(request, 'mapviewer/editar_yacimiento.html', {'form': form})

def buscador_yacimientos(request):
    tipos_yacimiento = TipoYacimiento.objects.all()
    tipos_fase_historica = TipoFaseHistorica.objects.all()
    return render(request,
                  'mapviewer/buscador_yacimientos.html',
                  {                   
                      'tipos_yacimento' : tipos_yacimiento,
                      'tipos_fase_historica' : tipos_fase_historica,
                  })


def opciones_provincia(request):
    comunidad_autonoma_id = request.GET.get('comunidad-autonoma-id')
    if comunidad_autonoma_id == '':
        provincias = Provincia.objects.none()
    else:
        provincias = Provincia.objects.filter(comunidad_autonoma_id=comunidad_autonoma_id).order_by('nombre')
    return render(request, 'mapviewer/dropdown_options.html', {'options': provincias})

def opciones_municipio(request):
    provincia_id = request.GET.get('provincia-id')
    if provincia_id == '':
        municipios = Municipio.objects.none()
    else:
        municipios = Municipio.objects.filter(provincia_id=provincia_id).order_by('nombre')
    return render(request, 'mapviewer/dropdown_options.html', {'options': municipios})
    


