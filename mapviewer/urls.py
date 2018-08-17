from django.urls import path
from mapviewer import views

urlpatterns = [
    path('', views.listado_yacimientos, name='listado_yacimientos'),
#     path('mapa/', views.mapa_yacimientos, name='mapa_Yacimientoes'),
    path('yacimiento/<int:pk>/', views.detalle_yacimiento, name='detalle_yacimiento'),
    path('yacimiento/nuevo/', views.nuevo_yacimiento, name='nuevo_yacimiento'),     
    path('yacimiento/<int:pk>/editar/', views.editar_yacimiento, name='editar_yacimiento'),
    path('yacimiento/buscador/', views.buscador_yacimientos, name='buscador_yacimientos'),
    path('ajax/opciones-provincia/', views.opciones_provincia, name='opciones_provincia'),
    path('ajax/opciones-municipio/', views.opciones_municipio, name='opciones_municipio'), 
]
