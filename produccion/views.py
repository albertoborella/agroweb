from django.shortcuts import render
from dateutil.parser import parse
from datetime import timedelta
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import ProdLeche,Alimento,ExistenciaTambo,ExistenciaRecria
from .forms import ProdLecheForm,AlimentoForm,ExistenciaTamboForm,ExistenciaRecriaForm,FechasForm

#====== Vistas de la aplicacion produccion =============
#====== Vistas para Produccion de Leche ================

# class ProdLecheList(ListView):
#     model = ProdLeche

# def Pl_fechas(request,inicio,fin):
#     form = FechasForm(request.POST)
    
#     if request.method == 'POST':
#         if form.is_valid():
#             inicio = form.cleaned_data['inicio']
#             fin = form.cleaned_data['final']
    
#     qs = ProdLeche.objects.filter(fecha__range=[inicio, fin])
    
#     suma = 0
#     for dato in qs:
#         d = dato.lts_total
#         suma = suma + d
#     ctx = {'qs': qs, 'suma': suma, 'form':form}
#     return render(request, 'produccion/prueba.html', ctx)  

def produccionleche_list(request):
    template_name = 'produccion/prodleche_list.html'
    object_list = ProdLeche.objects.all()
    

    start_date=request.GET.get('start_date')
    end_date=request.GET.get('end_date')

    if start_date and end_date:
        end_date = parse(end_date) # + timedelta(1) No hace falta porque toma un dia mas en el rango
        object_list = object_list.filter(
            fecha__range = [start_date,end_date]
        )

    suma = 0
    terneros = 0
    venta = 0
    for dato in object_list:
        d = dato.lts_total
        c = dato.consumo
        v = dato.venta
        suma = suma + d
        terneros = terneros + c
        venta = venta + v

    context = {'object_list': object_list, 'suma':suma, 'terneros':terneros, 'venta':venta}
    return render(request, template_name, context)

class ProdLecheCreate(CreateView):
    model = ProdLeche
    form_class = ProdLecheForm
    success_url = reverse_lazy('produccion:leche_list')

class ProdLecheUpdate(UpdateView):
    model = ProdLeche
    form_class = ProdLecheForm
    success_url = reverse_lazy('produccion:leche_list')

class ProdLecheDelete(DeleteView):
    model = ProdLeche
    success_url = reverse_lazy('produccion:leche_list')


#====== Vistas para Existencias ================

# class Existencia(ListView):
#     model = ExistenciaTambo
#     template_name = 'produccion/existenciatambo_list.html'

def existencia_list(request):
    template_name = 'produccion/existenciatambo_list.html'
    object_list = ExistenciaTambo.objects.all()

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

class ExistenciaCreate(CreateView):
    model = ExistenciaTambo
    form_class = ExistenciaTamboForm
    success_url = reverse_lazy('produccion:existenciatambo-list')

class ExistenciaUpdate(UpdateView):
    model = ExistenciaTambo
    form_class = ExistenciaTamboForm
    success_url = reverse_lazy('produccion:existenciatambo-list')

class ExistenciaDelete(DeleteView):
    model = ExistenciaTambo
    success_url =  reverse_lazy('produccion:existenciatambo-list')
#--------------------------------------------------------------------
# class Recria(ListView):
#     model = ExistenciaRecria
#     template_name = 'produccion/existenciarecria_list.html'

def recria_list(request):
    template_name = 'produccion/existenciarecria_list.html'
    object_list = ExistenciaRecria.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        # Converte em data e adiciona um dia.
        end_date = parse(end_date) 
        object_list = object_list.filter(
            fecha__range = [start_date, end_date]
         )

    context = {'object_list':object_list}
    return render(request, template_name, context)

class RecriaCreate(CreateView):
    model = ExistenciaRecria
    form_class = ExistenciaRecriaForm
    success_url = reverse_lazy('produccion:recria-list')

class RecriaUpdate(UpdateView):
    model = ExistenciaRecria
    form_class = ExistenciaRecriaForm
    success_url = reverse_lazy('produccion:recria-list')

class RecriaDelete(DeleteView):
    model = ExistenciaRecria
    success_url =  reverse_lazy('produccion:recria-list')  

#====== Vistas para Tipos de Alimentos ================

class AlimentoList(ListView):
    model = Alimento
    template_name = 'produccion/alimento/alimento_list.html'

class AlimentoCreate(CreateView):
    model = Alimento
    form_class = AlimentoForm
    template_name = 'produccion/alimento/alimento_form.html'
    success_url = reverse_lazy('produccion:alimento')

class AlimentoUpdate(UpdateView):
    model = Alimento
    form_class = AlimentoForm
    template_name = 'produccion/alimento/alimento_form.html'
    success_url = reverse_lazy('produccion:alimento')

class AlimentoDelete(DeleteView):
    model = Alimento
    template_name = 'produccion/alimento/alimento_confirm_delete.html'
    success_url = reverse_lazy('produccion:alimento')

   