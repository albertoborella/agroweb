from django.urls import path
from .views import VistaRegistro,salir,acceder,index

urlpatterns = [
    path('register/', VistaRegistro.as_view(), name='register'),
    path('', acceder, name='acceder'),
    path('index/', index, name='index'),
    path('salir/', salir, name='salir'),
]