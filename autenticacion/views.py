from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages


def index(request):
    return render(request, 'autenticacion/index.html', {})

def acceder(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                # messages.success(request, f"Bienvenido a la plataforma de AgroWeb")
                return redirect('index')
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")

    form = AuthenticationForm()
    return render(request, 'autenticacion/acceder.html', {'form':form })

class VistaRegistro(View):
    
    def get(self,request):
        form = UserCreationForm()
        return render(request, 'autenticacion/register.html', {'form':form})

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            messages.success(request, f"Bienvenido a la plataforma {nombre_usuario}")
            login(request, usuario)
            return redirect('index')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'autenticacion/register.html', {'form':form})

def salir(request):

    logout(request)
    messages.success(request, f"Tu sesion se ha cerrado correctamente")
    return redirect('acceder')
