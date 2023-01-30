from django.urls import path
from .views import EmpleadoCrear, EmpleadoDelete, EmpleadoEdit, EmpleadoList, GastosList, RubroGastoList,RubroGastoEdit,RubroGastoCrear,RubroGastoDelete, RubroVentaEdit,RubroVentaList,RubroVentaCrear,RubroVentaDelete,SubrubroGastoList,SubrubroGastoCrear,SubrubroGastoEdit,SubrubroGastoDelete, UmedidaList,UmedidaCrear,UmedidaEdit,UmedidaDelete,ClienteList,ClienteCrear,ClienteEdit,ClienteDelete,ProveedorList,ProveedorCrear,ProveedorEdit,ProveedorDelete,GastosList,GastoCrear,GastoEdit,GastoDelete,listado_gastos, listado_gastos_alimentacion, listado_gastos_combustibles,listado_gastos_sanidad,listado_gastos_pasturas,listado_gastos_estructuras,listado_gastos_repmaq,listado_gastos_servicios



app_name = 'economico'

urlpatterns = [
    path('rubro/gastos/', RubroGastoList.as_view(), name='rubro-gasto'),
    path('rubro/gastos/crear/', RubroGastoCrear.as_view(), name='rubro-gasto-crear'),
    path('rubro/gastos/editar/<int:pk>/', RubroGastoEdit.as_view(), name='rubro-gasto-edit'),
    path('rubro/gastos/borrar/<int:pk>/', RubroGastoDelete.as_view(), name='rubro-gasto-delete'),

    path('subrubro/gastos/', SubrubroGastoList.as_view(), name='subrubro-gasto'),
    path('subrubro/gastos/crear/', SubrubroGastoCrear.as_view(), name='subrubro-gasto-crear'),
    path('subrubro/gastos/editar/<int:pk>/', SubrubroGastoEdit.as_view(), name='subrubro-gasto-edit'),
    path('subrubro/gastos/borrar/<int:pk>/', SubrubroGastoDelete.as_view(), name='subrubro-gasto-delete'),

    path('rubro/ventas/', RubroVentaList.as_view(), name='rubro-venta'),
    path('rubro/ventas/crear/', RubroVentaCrear.as_view(), name='rubro-venta-crear'),
    path('rubro/ventas/editar/<int:pk>/', RubroVentaEdit.as_view(), name='rubro-venta-edit'),
    path('rubro/ventas/borrar/<int:pk>/', RubroVentaDelete.as_view(), name='rubro-venta-delete'),

    path('datos/u_medida/', UmedidaList.as_view(), name='dato-umedida'),
    path('datos/u_medida/crear/', UmedidaCrear.as_view(), name='dato-umedida-crear'),
    path('datos/u_medida/editar/<int:pk>/', UmedidaEdit.as_view(), name='dato-umedida-edit'),
    path('datos/u_medida/borrar/<int:pk>/', UmedidaDelete.as_view(), name='dato-umedida-delete'),

    path('datos/empleados/', EmpleadoList, name='dato-empleado'),
    path('datos/empleados/crear/', EmpleadoCrear.as_view(), name='dato-empleado-crear'),
    path('datos/empleados/editar/<int:pk>/', EmpleadoEdit.as_view(), name='dato-empleado-edit'),
    path('datos/empleados/borrar/<int:pk>/', EmpleadoDelete.as_view(), name='dato-empleado-delete'),

    path('datos/clientes/', ClienteList, name='dato-cliente'),
    path('datos/clientes/crear/', ClienteCrear.as_view(), name='dato-cliente-crear'),
    path('datos/clientes/editar/<int:pk>/', ClienteEdit.as_view(), name='dato-cliente-edit'),
    path('datos/clientes/borrar/<int:pk>/', ClienteDelete.as_view(), name='dato-cliente-delete'),

    path('datos/proveedores/', ProveedorList, name='dato-proveedor'),
    path('datos/proveedores/crear/', ProveedorCrear.as_view(), name='dato-proveedor-crear'),
    path('datos/proveedores/editar/<int:pk>/', ProveedorEdit.as_view(), name='dato-proveedor-edit'),
    path('datos/proveedores/borrar/<int:pk>/', ProveedorDelete.as_view(), name='dato-proveedor-delete'),

    path('gastos/', GastosList, name='gasto'),
    path('listado/gastos/', listado_gastos, name='listado-gastos'),
    path('listado/gastos/alimentacion/', listado_gastos_alimentacion, name='listado-gastos-alimentacion'),
    path('listado/gastos/sanidad/', listado_gastos_sanidad, name='listado-gastos-sanidad'),
    path('listado/gastos/servicios/', listado_gastos_servicios, name='listado-gastos-servicios'),
    path('listado/gastos/combustibles/', listado_gastos_combustibles, name='listado-gastos-combustibles'),
    path('listado/gastos/pasturas/', listado_gastos_pasturas, name='listado-gastos-pasturas'),
    path('listado/gastos/estructuras/', listado_gastos_estructuras, name='listado-gastos-estructuras'),
    path('listado/gastos/rep.maquinarias/', listado_gastos_repmaq, name='listado-gastos-repmaq'),
    path('gastos/nuevo/', GastoCrear.as_view(), name='gasto-crear'),
    path('gastos/editar/<int:pk>/', GastoEdit.as_view(), name='gasto-edit'),
    path('gastos/eliminar/<int:pk>/', GastoDelete.as_view(), name='gasto-delete'),
]
