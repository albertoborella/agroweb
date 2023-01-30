from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from dateutil.parser import parse
from datetime import timedelta
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import RubroGasto,RubroVenta,Subrubro,Umedida,Empleado,Cliente,Proveedor,Gasto
from .forms import RubroGastoForm,RubroVentaForm,SubRubroGastoForm,UmedidaForm,EmpleadoForm,ClienteForm,ProveedorForm,GastoForm
# Datos de configuración -----------------------------------------------------------
class RubroGastoList(ListView):
    model = RubroGasto

class RubroGastoCrear(CreateView):
    model = RubroGasto
    form_class = RubroGastoForm
    success_url = reverse_lazy('economico:rubro-gasto')
    template_name = 'economico/rubrogasto_crear.html'

    def post(self,request,*args,**kwargs):
        print(request.POST)
        form = RubroGastoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None    
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, 'economico/rubrogasto_crear.html', context)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Categoria de Gastos'
        context['entity'] = 'Categoría-Gastos'
        # context['list_url'] = reverse_lazy('economico:rubro-gasto')
        return context

class RubroGastoEdit(UpdateView):
    model = RubroGasto
    form_class = RubroGastoForm
    success_url = reverse_lazy('economico:rubro-gasto')

class RubroGastoDelete(DeleteView):
    model = RubroGasto
    form_class = RubroGastoForm
    success_url = reverse_lazy('economico:rubro-gasto')

class RubroVentaList(ListView):
    model = RubroVenta

class RubroVentaCrear(CreateView):
    model = RubroVenta
    form_class = RubroVentaForm
    success_url = reverse_lazy('economico:rubro-venta')

class RubroVentaEdit(UpdateView):
    model = RubroVenta
    form_class = RubroVentaForm
    success_url = reverse_lazy('economico:rubro-venta')

class RubroVentaDelete(DeleteView):
    model = RubroVenta
    form_class = RubroVentaForm
    success_url = reverse_lazy('economico:rubro-venta') 

class SubrubroGastoList(ListView):
    model = Subrubro
    template_name = 'economico/subrubro_list.html'

class SubrubroGastoCrear(CreateView):
    model = Subrubro
    form_class = SubRubroGastoForm
    success_url = reverse_lazy('economico:subrubro-gasto')

class SubrubroGastoEdit(UpdateView):
    model = Subrubro
    form_class = SubRubroGastoForm
    success_url = reverse_lazy('economico:subrubro-gasto')

class SubrubroGastoDelete(DeleteView):
    model = Subrubro
    form_class = SubRubroGastoForm
    success_url = reverse_lazy('economico:subrubro-gasto') 

class UmedidaList(ListView):
    model = Umedida

class UmedidaCrear(CreateView):
    model = Umedida
    form_class = UmedidaForm
    success_url = reverse_lazy('economico:dato-umedida')

class UmedidaEdit(UpdateView):
    model = Umedida
    form_class = UmedidaForm
    success_url = reverse_lazy('economico:dato-umedida')

class UmedidaDelete(DeleteView):
    model = Umedida
    form_class = UmedidaForm
    success_url = reverse_lazy('economico:dato-umedida')

def EmpleadoList(request):
    empleados = Empleado.objects.filter(estado=True)
    return render(request, 'economico/empleado_list.html', {'empleados':empleados})

class EmpleadoCrear(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('economico:dato-empleado')

class EmpleadoEdit(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('economico:dato-empleado')

class EmpleadoDelete(DeleteView):
    model = Empleado

    def post(self,request, pk,*args,**kwargs):
        object = Empleado.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('economico:dato-empleado')

def ProveedorList(request):
    proveedores = Proveedor.objects.filter(estado=True)
    return render(request, 'economico/proveedor_list.html', {'proveedores':proveedores})

class ProveedorCrear(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    success_url = reverse_lazy('economico:dato-proveedor')

class ProveedorEdit(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    success_url = reverse_lazy('economico:dato-proveedor')

class ProveedorDelete(DeleteView):
    model = Proveedor

    def post(self,request, pk,*args,**kwargs):
        object = Proveedor.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('economico:dato-proveedor')

def ClienteList(request):
    clientes = Cliente.objects.filter(estado=True)
    return render(request, 'economico/cliente_list.html', {'clientes':clientes})

class ClienteCrear(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('economico:dato-cliente')

class ClienteEdit(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('economico:dato-cliente')

class ClienteDelete(DeleteView):
    model = Cliente

    def post(self,request, pk,*args,**kwargs):
        object = Cliente.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('economico:dato-cliente')

# Datos de carga de gastos e ingresos -------------------------------------------------

def GastosList(request):
    gastos = Gasto.objects.filter(estado=True)
    return render(request, 'economico/gasto_list.html', {'gastos':gastos})

def listado_gastos(request):
    template_name = 'economico/listado_gastos.html'
    object_list = Gasto.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Converte em data e adiciona um dia.
        end_date = parse(end_date) + timedelta(1)
        object_list = object_list.filter(
            fecha__range = [start_date, end_date]
         )

    context = {'object_list':object_list}
    return render(request, template_name, context)

def listado_gastos_alimentacion(request):
    template_name = 'economico/listado_gastos_alimentacion.html'
    object_list = Gasto.objects.all().filter(rubro_id=1)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Converte em data e adiciona um dia.
        end_date = parse(end_date) + timedelta(1)
        object_list = object_list.filter(
            fecha__range = [start_date, end_date]
         )

    context = {'object_list':object_list}
    return render(request, template_name, context)

def listado_gastos_sanidad(request):
    template_name = 'economico/listado_gastos_sanidad.html'
    object_list = Gasto.objects.all().filter(rubro_id=2)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Converte em data e adiciona um dia.
        end_date = parse(end_date) + timedelta(1)
        object_list = object_list.filter(
            fecha__range = [start_date, end_date]
         )

    context = {'object_list':object_list}
    return render(request, template_name, context)

def listado_gastos_pasturas(request):
    template_name = 'economico/listado_gastos_pasturas.html'
    object_list = Gasto.objects.all().filter(rubro_id=3)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Converte em data e adiciona um dia.
        end_date = parse(end_date) + timedelta(1)
        object_list = object_list.filter(
            fecha__range = [start_date, end_date]
         )

    context = {'object_list':object_list}
    return render(request, template_name, context)

def listado_gastos_combustibles(request):
    template_name = 'economico/listado_gastos_combustibles.html'
    object_list = Gasto.objects.all().filter(rubro_id=4)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Converte em data e adiciona um dia.
        end_date = parse(end_date) + timedelta(1)
        object_list = object_list.filter(
            fecha__range = [start_date, end_date]
         )

    context = {'object_list':object_list}
    return render(request, template_name, context)

def listado_gastos_estructuras(request):
    template_name = 'economico/listado_gastos_estructuras.html'
    object_list = Gasto.objects.all().filter(rubro_id=5)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Converte em data e adiciona um dia.
        end_date = parse(end_date) + timedelta(1)
        object_list = object_list.filter(
            fecha__range = [start_date, end_date]
         )

    context = {'object_list':object_list}
    return render(request, template_name, context)

def listado_gastos_repmaq(request):
    template_name = 'economico/listado_gastos_repmaq.html'
    object_list = Gasto.objects.all().filter(rubro_id=6)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Converte em data e adiciona um dia.
        end_date = parse(end_date) + timedelta(1)
        object_list = object_list.filter(
            fecha__range = [start_date, end_date]
         )

    context = {'object_list':object_list}
    return render(request, template_name, context)

def listado_gastos_servicios(request):
    template_name = 'economico/listado_gastos_servicios.html'
    object_list = Gasto.objects.all().filter(rubro_id=7)

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Converte em data e adiciona um dia.
        end_date = parse(end_date) + timedelta(1)
        object_list = object_list.filter(
            fecha__range = [start_date, end_date]
         )

    context = {'object_list':object_list}
    return render(request, template_name, context)

class GastoCrear(CreateView):
    model = Gasto
    form_class = GastoForm
    success_url = reverse_lazy('economico:gasto')

class GastoEdit(UpdateView):
    model = Gasto
    form_class = GastoForm
    success_url = reverse_lazy('economico:gasto')

class GastoDelete(DeleteView):
    model = Gasto

    def post(self,request, pk,*args,**kwargs):
        object = Gasto.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('economico:gasto')