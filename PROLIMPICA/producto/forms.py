from django import forms
from modelo.models import Producto
from dataclasses import fields

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["id", "nombres","precio", "tipoProduct","marca","fechaCaducidad" ]
        widgets = {
            'id': forms.TextInput(attrs={'placeholder':'Ingrese id', 'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'placeholder':'Ingrese Nombres', 'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'placeholder':'Ingrese Precio', 'class': 'form-control'}),
            'tipoProduct': forms.RadioSelect(attrs={'class': "form-check-input"}),
            'marca': forms.RadioSelect(attrs={'class': "form-check-input"}),
            'fechaCaducidad': forms.TextInput(attrs={'placeholder':'Ingrese Fecha Caducidad', 'class': 'form-control'}),
        }
