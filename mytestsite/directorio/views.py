from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from .models import *
from directorio.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import *
from django.contrib import messages
import calendar
import datetime
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.forms import  UserCreationForm, UserChangeForm, PasswordChangeForm

from django.contrib.auth import update_session_auth_hash



class Round(Func):
  function = 'ROUND'
  arity = 2

def cambio_pass(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)

			return render(request, 'cambio_pass.html',context={'cambiado':'Password Cambiado'})
			#messages.success(request,'Contra cambiada')
			#return redirect('logout')
		else:
			return render(request, 'cambio_pass.html', context={'error':'Corrija los datos', 'form':form})
			#messages.error(request, 'Corrija el error')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'cambio_pass.html', {'form': form})




def login(request):
	return render(request, template_name= 'login.html', context={'login': login})


def index(request):
	return render(request, template_name= 'index.html', context={'index': index})

def base_usuarios(request):
	return render(request, template_name= 'base_usuarios.html')


def graficas_municipales(request):
	ahora = datetime.datetime.now()
	meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
	mes = meses[ahora.month -1]


	condicion = Q(municipio__usuario__id=request.user.id,atendido='si')
	
	if request.user.groups.filter(name ='Instructores').exists():
		pedidos = pedido.objects.filter(condicion).order_by('date__month').values('date__month').annotate(recaudacion=Sum('sub_total'))
		return HttpResponse(json.dumps(list(pedidos), cls=DjangoJSONEncoder))
	
	else:
		pedidos = pedido.objects.filter(atendido='si').order_by('date__month').values('date__month').annotate(recaudacion=Sum('sub_total'))
		return HttpResponse(json.dumps(list(pedidos), cls=DjangoJSONEncoder))





def graficas_provinciales(request):
	ahora = datetime.datetime.now()
	mes=ahora.month
	condicion = Q(provincia__usuario__id=request.user.id,atendido='si')
	if request.user.groups.filter(name ='Directores').exists():
		pedidos = pedido.objects.filter(condicion,date__month=mes).order_by('date__month','municipio').values('municipio__municipio').annotate(recaudacion=Sum('sub_total'))
		return HttpResponse(json.dumps(list(pedidos), cls=DjangoJSONEncoder))
	else:
		pedidos = pedido.objects.filter(atendido='si',date__month=mes).order_by('date__month','municipio').values('municipio__municipio','date__month').annotate(recaudacion=Sum('sub_total'))
		return HttpResponse(json.dumps(list(pedidos), cls=DjangoJSONEncoder))









def list_servicios(request):
	servicios = servicio.objects.all()
	return render(request, template_name= 'list_servicios.html', context={'servicios': servicios})



def instructores(request):
	return render(request, template_name= 'instructores.html')



def por_atender(request):
	#condicion = Q(municipio__usuario__id=request.user.id,atendido='no')

	if request.user.groups.filter(name ='Instructores').exists():
		
		datos=list(pedido.objects.filter(municipio__usuario__id=request.user.id,atendido='no').order_by('date','carnet').values('carnet','date','nombre','apellido1','apellido2').annotate(total=Sum('sub_total'),contratos=Count('id')))

		return HttpResponse(json.dumps(datos,cls=DjangoJSONEncoder))
	
	else:
		
		datos=list(pedido.objects.filter(atendido='no').order_by('date', 'carnet').values('carnet','date','nombre','apellido1','apellido2').annotate(total=Sum('sub_total'),contratos=Count('id')))
		
		return HttpResponse(json.dumps(datos,cls=DjangoJSONEncoder))
		
		
def clientes_atendidos(request):
	return render(request, template_name= 'clientes_atendidos.html')


def atendidos(request):
	#condicion = Q(municipio__usuario__id=request.user.id,atendido='si')

	if request.user.groups.filter(name ='Instructores').exists():
		datos=list(pedido.objects.filter(municipio__usuario__id=request.user.id,atendido='si').order_by('date','carnet').values('carnet','date','nombre','apellido1','apellido2').annotate(total=Sum('sub_total'),contratos=Count('id')))
		return HttpResponse(json.dumps(datos,cls=DjangoJSONEncoder))
	else:

		datos=list(pedido.objects.filter(atendido='si').order_by('date', 'carnet').values('carnet','date','nombre','apellido1','apellido2').annotate(total=Sum('sub_total'),contratos=Count('id')))

		return HttpResponse(json.dumps(datos,cls=DjangoJSONEncoder))



def contador_atendidos(request):

	if request.user.groups.filter(name ='Instructores').exists():
		pedidos = pedido.objects.filter(municipio__usuario__id=request.user.id,atendido='si').order_by('date','carnet').values('carnet','nombre').annotate(contratos=Count('id')).count()

		return HttpResponse(json.dumps(pedidos, cls=DjangoJSONEncoder))
	else:



		pedidos = pedido.objects.filter(atendido='si').order_by('date','carnet').values('carnet','nombre').annotate(contratos=Count('id')).count()				
		return HttpResponse(json.dumps(pedidos, cls=DjangoJSONEncoder))





def buscador(request, fecha1,fecha2):
	
	condicion1 = Q(municipio__usuario__id=request.user.id,atendido='si')
	
	if request.user.groups.filter(name = 'Instructores').exists():
		datos = list(pedido.objects.filter(condicion1, date__range=[fecha1,fecha2]).order_by('date','carnet').values('carnet','nombre','apellido1','apellido2', 'date').annotate(total=Sum('sub_total'),contratos=Count('id')))
		return HttpResponse(json.dumps(datos,cls=DjangoJSONEncoder))
	else:
		datos = list(pedido.objects.filter(atendido='si', date__range=[fecha1,fecha2]).order_by('date','carnet').values('carnet','nombre','apellido1','apellido2', 'date').annotate(total=Sum('sub_total'),contratos=Count('id')))
		return HttpResponse(json.dumps(datos,cls=DjangoJSONEncoder))




def atender_usuario(request,carnet,date):
	
	pedido.objects.filter(carnet=carnet,date=date).update(atendido='si')
	pedido.save()
	return render(request, template_name= 'instructores.html', context={'atendido': 'Se atendio el usuario'})





def municipio_provincia(request, id_provincia):
	prov = provincia.objects.filter(id=id_provincia).select_related('municipio').values('municipio__municipio','municipio__id')
	return HttpResponse(json.dumps(list(prov), cls=DjangoJSONEncoder))
    



def procesar(request):
	form = pedidoForm(request.POST)
	#serv= servicio.objects.filter(temporal='si')
	return render(request, template_name= 'procesar.html', context= {'form':form})




def pedidoCreate(request):
	if request.method == 'POST':
		form = pedidoForm(request.POST)
		data=list(json.loads(request.POST['servicios']))
		lis=[]
		for x in data:
			p= pedido()			
			p.nombre=request.POST['nombre']
			p.carnet=request.POST['carnet']
			p.apellido1=request.POST['apellido1']
			p.apellido2=request.POST['apellido2']
			p.provincia=provincia.objects.get(id=request.POST['provincia'])
			p.municipio=municipio.objects.get(id=request.POST['municipio'])
			p.direccion=request.POST['direccion']
			p.servicio=servicio.objects.get(id=x['id_servicio'])
			p.sub_total=x['subtotal']
			p.cantidad=x['cantidad']
			p.atendido='no'
			p.save() 		
		
		return redirect('list_servicios')


	else:
		form = pedidoForm()
	return render(request, 'procesar.html', {'form':form})




def detalles_modal_atendidos(request, carnet, date):
	datos=list(pedido.objects.filter(carnet=carnet,date=date,atendido='si').order_by('date','carnet').values('carnet','nombre','apellido1','apellido2','direccion').annotate(total=Sum('sub_total'),cantidad=Sum('cantidad')))
	
	return HttpResponse(json.dumps(datos,cls=DjangoJSONEncoder))

def detalles_modal_atender(request, carnet, date):
	datos=list(pedido.objects.filter(carnet=carnet,date=date,atendido='no').order_by('date','carnet').values('carnet','nombre','apellido1','apellido2','direccion').annotate(total=Sum('sub_total'),cantidad=Sum('cantidad')))
	
	return HttpResponse(json.dumps(datos,cls=DjangoJSONEncoder))



def detalles_modal_servicio(request, carnet, date):	
	datos = pedido.objects.filter(carnet=carnet,date=date,atendido='si').order_by('date','carnet').values('servicio_id','cantidad').annotate(total=Sum('sub_total'))
	lis=[]
	for x in datos:
		
		ser = servicio.objects.get(id=x['servicio_id'])
		data=dict()
		data=model_to_dict(ser)
		lis.append(data)
	return HttpResponse(json.dumps(lis,cls=DjangoJSONEncoder))

def detalles_modal_servicio_atender(request, carnet, date):	
	datos = pedido.objects.filter(carnet=carnet,date=date,atendido='no').order_by('date','carnet').values('servicio_id','cantidad').annotate(total=Sum('sub_total'))
	lis=[]
	for x in datos:
		
		ser = servicio.objects.get(id=x['servicio_id'])
		data=dict()
		data=model_to_dict(ser)
		lis.append(data)
	return HttpResponse(json.dumps(lis,cls=DjangoJSONEncoder))

def cantidades(request, carnet, date):
    datos = pedido.objects.filter(carnet=carnet,date=date,atendido='si').order_by('date','carnet').values('servicio_id','cantidad').annotate(total=Sum('sub_total'))
    p= []
    for x in datos:
    	p.append(x['cantidad'])
    return HttpResponse(json.dumps(p,cls=DjangoJSONEncoder))

def cantidades_atender(request, carnet, date):
    datos = pedido.objects.filter(carnet=carnet,date=date,atendido='no').order_by('date','carnet').values('servicio_id','cantidad').annotate(total=Sum('sub_total'))
    p= []
    for x in datos:
    	p.append(x['cantidad'])
    return HttpResponse(json.dumps(p,cls=DjangoJSONEncoder))





def contador_atendidos_municipios(request):
	pedidos = pedido.objects.filter(provincia__usuario__id=request.user.id,atendido='si').order_by('date','carnet').values('carnet','nombre','municipio').annotate(contratos=Count('id'))

	return HttpResponse(pedidos)




def agregar_carrito(request, id):
    ser = servicio.objects.get(id=id)
    data=dict()
    data['servicio']=model_to_dict(ser)
    return JsonResponse(data) 



def cargar_servicios(request, servicios):
   servicios=servicios.split(',')
   data=list(servicio.objects.filter(id__in=servicios).values('id','nomb_servicio','descripcion','precio'))
   #id_in pq servicios es un array 
   return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder))



def cargar_envio(request, servicios):
   servicios=servicios.split(',')
   data=list(servicio.objects.all())
   #id_in pq servicios es un array 
   return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder))


def contador_atender(request):

	if request.user.groups.filter(name ='Instructores').exists():
		pedidos = pedido.objects.filter(municipio__usuario__id=request.user.id,atendido='no').order_by('date','carnet').values('carnet','nombre').annotate(contratos=Count('id')).count()

		return HttpResponse(json.dumps(pedidos, cls=DjangoJSONEncoder))
	else:

		pedidos = pedido.objects.filter(atendido='no').order_by('date','carnet').values('carnet','nombre').annotate(contratos=Count('id')).count()

		return HttpResponse(json.dumps(pedidos, cls=DjangoJSONEncoder))

