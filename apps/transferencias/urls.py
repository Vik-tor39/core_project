from django.urls import path, include
from . import views

urlpatterns = [
    path('sugerencias/', views.panel_sugerencias, name='panel_sugerencias'),
    path('sugerencias/<int:sug_id>/aceptar/', views.aceptar_sugerencia, name='aceptar_sugerencia'),
]
