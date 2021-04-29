from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class pedidoForm(forms.ModelForm):
	class Meta:
		model = pedido
		fields = '__all__'

		widgets ={
		          'carnet': forms.Select(attrs={'class': 'form-control form-select2', 'onkeypress':'return solonumeros(event)'}),
		          'nombre': forms.Select(attrs={'class': 'form-control form-select2', 'onkeypress':'return sololetras(event)'}),
		          'apellido1': forms.Select(attrs={'class': 'form-control form-select2', 'onkeypress':'return sololetras(event)'}),
		          'apellido2': forms.Select(attrs={'class': 'form-control form-select2', 'onkeypress':'return sololetras(event)'}),
		          'provincia': forms.Select(attrs={'class': 'form-control form-select2'}),
		          'municipio': forms.Select(attrs={'class': 'form-control form-select2'}),
		          'direccion': forms.TextInput(attrs={'class': 'form-control'}),
		          'servicios': forms.TextInput(attrs={'class': 'form-control'}),
		          'atendido': forms.TextInput(attrs={'class': 'form-control'}),
                  
 
		         # 'cantidad': forms.IntInput(attrs={'class': 'form-control'}),
		          }



