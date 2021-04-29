from django.urls import *
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from directorio import views

from .views import *

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^base_usuarios/', views.base_usuarios, name='base_usuarios'),
   
    url(r'^login/', views.login, name='login'),
   
    url(r'^cambio_pass/', views.cambio_pass, name='cambio_pass'),
   

    url(r'^buscador/(?P<fecha1>[\w\-]+)/(?P<fecha2>[\w\-]+)/$', buscador, name='buscador'),





    url(r'^graficas_municipales/', graficas_municipales, name='graficas_municipales'),
    
    url(r'^list_servicios/', list_servicios, name='list_servicios'),

    url(r'^instructores/', instructores, name='instructores'),

    url(r'^por_atender/', por_atender, name='por_atender'),

    url(r'^clientes_atendidos/', clientes_atendidos, name='clientes_atendidos'),

    url(r'^atendidos/', atendidos, name='atendidos'),

    url(r'^atender_usuario/(?P<carnet>\d+)/(?P<date>[\w\-]+)/$', atender_usuario, name='atender_usuario'),

    url(r'^municipio_provincia/(?P<id_provincia>\d+)/$', municipio_provincia, name='municipio_provincia'),
   
   

    url(r'^procesar/', procesar, name='procesar'),
    
    url(r'^pedido/', pedidoCreate, name='pedido'),

    url(r'^detalles_modal_atendidos/(?P<carnet>\d+)/(?P<date>[\w\-]+)/$', detalles_modal_atendidos, name='detalles_modal_atendidos'),
    url(r'^detalles_modal_atender/(?P<carnet>\d+)/(?P<date>[\w\-]+)/$', detalles_modal_atender, name='detalles_modal_atender'),
    url(r'^detalles_modal_servicio/(?P<carnet>\d+)/(?P<date>[\w\-]+)/$', detalles_modal_servicio, name='detalles_modal_servicio'),
    url(r'^detalles_modal_servicio_atender/(?P<carnet>\d+)/(?P<date>[\w\-]+)/$', detalles_modal_servicio_atender, name='detalles_modal_servicio_atender'),
    url(r'^cantidades/(?P<carnet>\d+)/(?P<date>[\w\-]+)/$', cantidades, name='cantidades'),
    url(r'^cantidades_atender/(?P<carnet>\d+)/(?P<date>[\w\-]+)/$', cantidades_atender, name='cantidades_atender'),
    url(r'^agregar_carrito/(?P<id>\d+)/$', agregar_carrito, name='agregar_carrito'),

    url(r'^cargar_servicios/(?P<servicios>[\w\,]+)/$', cargar_servicios, name='cargar_servicios'),

    url(r'^cargar_envio/(?P<servicios>[\w\,]+)/$', cargar_envio, name='cargar_envio'),

   # url(r'^enviar_pedido/(?P<carnet>[\d+)/(?P<date>[\w\-]+)/$', login_required(enviar_pedido), name='enviar_pedido'),

    url(r'^contador_atender/', contador_atender, name='contador_atender'),

    url(r'^contador_atendidos/', contador_atendidos, name='contador_atendidos'),

    url(r'^graficas_provinciales/', graficas_provinciales, name='graficas_provinciales'),

 

    
  
 ]   