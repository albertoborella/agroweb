from django.urls import path
from .views import *

app_name = 'produccion'

urlpatterns = [
    path('leche/', produccionleche_list, name='leche_list'),
    path('leche/registro/', ProdLecheCreate.as_view(), name='leche-create'),
    path('leche/registro/modificar/<int:pk>/', ProdLecheUpdate.as_view(), name='leche-edit'),
    path('leche/registro/eliminar/<int:pk>/', ProdLecheDelete.as_view(), name='leche-delete'),
    # path('leche/<str:inicio>/<str:fin>/', Pl_fechas, name='leche_list_fechas'),

    path('alimentos/', AlimentoList.as_view(), name='alimento'),
    path('alimentos/crear/', AlimentoCreate.as_view(), name='alimento-crear'),
    path('alimentos/modificar/<int:pk>/', AlimentoUpdate.as_view(), name='alimento-edit'),
    path('alimentos/eliminar/<int:pk>/', AlimentoDelete.as_view(), name='alimento-delete'),

    # path('existencias/', Existencia.as_view(), name='existenciatambo-list'),
    path('existencias/', existencia_list, name='existenciatambo-list'),
    path('existencias/crear/', ExistenciaCreate.as_view(), name='existenciatambo-crear'),
    path('existencias/modificar/<int:pk>/', ExistenciaUpdate.as_view(), name='existenciatambo-edit'),
    path('existencias/eliminar/<int:pk>/', ExistenciaDelete.as_view(), name='existenciatambo-delete'),

    path('recria/', recria_list, name='recria-list'),
    path('recria/crear/', RecriaCreate.as_view(), name='recria-crear'),
    path('recria/modificar/<int:pk>/', RecriaUpdate.as_view(), name='recria-edit'),
    path('recria/eliminar/<int:pk>/', RecriaDelete.as_view(), name='recria-delete'),
]
