from django.contrib import admin
from .models import *
#from easy_select2 import select2_modelform


admin.site.site_header = "Servicios"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"

# Register your models here.




#instructorForm = select2_modelform(instructor, attrs={'width': '250px'})
class instructorAdmin(admin.ModelAdmin):
	list_display=['usuario_instructor']
#	form=instructorForm
admin.site.register(instructor,instructorAdmin)



#servicioForm = select2_modelform(servicio, attrs={'width': '250px'})
class servicioAdmin(admin.ModelAdmin):
	list_display=('nomb_servicio', 'precio')
#	form=servicioForm
admin.site.register(servicio,servicioAdmin)



#municipioForm = select2_modelform(municipio, attrs={'width': '250px'})
class municipioAdmin(admin.ModelAdmin):
	list_display=['municipio']
#	form=municipioForm
admin.site.register(municipio,municipioAdmin)


#provinciaForm = select2_modelform(provincia, attrs={'width': '250px'})
class provinciaAdmin(admin.ModelAdmin):
	list_display=['provincia']
#	form=provinciaForm
admin.site.register(provincia,provinciaAdmin)





#pedidoForm = select2_modelform(pedido, attrs={'width': '250px'})
class pedidoAdmin(admin.ModelAdmin):
	list_display=('sub_total','carnet','nombre','apellido1','apellido2','direccion','date','atendido')
#	form=pedidoForm
admin.site.register(pedido,pedidoAdmin)
#temporalForm = select2_modelform(temporal, attrs={'width': '250px'})
#class temporalAdmin(admin.ModelAdmin):
#	list_display=('nomb_servicio', 'precio')
#	form=temporalForm
#admin.site.register(temporal,temporalAdmin)


