from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from modelo.models import Producto
from .forms import ClienteFormulario
from django.contrib.auth.models import User, Group

# Create your views here.
def index(request):
    listaCliente = Producto.objects.all().order_by('apellidos')
    return render(request,'clientes/principal.html', locals())
    return render(request,'clientes/principal.html')
    

def guardar(request):
    
    
    
    formulario_cliente = ClienteFormulario(request.POST)
    if request.method == 'POST':
        if formulario_cliente.is_valid() :
            cliente = Producto()
            datos_cliente = formulario_cliente.cleaned_data
            cliente.id = datos_cliente.get('id')
            cliente.nombres = datos_cliente.get('nombres')
            cliente.tipoProduct = datos_cliente.get('tipoProduct')
           
            cliente.save()
            
            return redirect(index)
    return render(request, 'clientes/guiRegistrarCliente.html', locals())
    