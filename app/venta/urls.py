from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.producto, name='productos'),
    path('productos/nuevo', views.nuevo_producto, name='producto-nuevo'),
]
