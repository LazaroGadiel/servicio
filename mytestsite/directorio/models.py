from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# Create your models here.


class instructor(models.Model):
      id= models.AutoField(primary_key=True)
      usuario_instructor= models.CharField(max_length=255)
      #centro= models.CharField(max_length=255)

      class Meta:
            verbose_name = 'Instructor'
            verbose_name_plural = 'Instructores'
      def __str__(self):
            return u'{}'.format(self.usuario_instructor)









class servicio(models.Model):
      id= models.AutoField(primary_key=True)
      nomb_servicio= models.CharField(max_length=255)
      precio= models.IntegerField()
      descripcion = models.CharField(max_length=255)
    
      

      class Meta:
            verbose_name = 'Servicio'
            verbose_name_plural = 'Servicios'
      def __str__(self):
            return u'{}'.format(self.nomb_servicio)


class municipio(models.Model):
      id= models.AutoField(primary_key=True)
      municipio= models.CharField(max_length=255,blank=True, choices=(('Candelaria','Candelaria'),('S. Cristóbal','S. Cristóbal'),('Alquízar','Alquízar'),('Bahía Honda','Bahía Honda'),('Artemisa','Artemisa'),('Guira de Melena','Guira de Melena'),
        ('S.A. Baños','S.A. Baños'),('Bauta','Bauta'),('Caimito','Caimito'),('Guanajay','Guanajay'),('Mariel','Mariel'),))
      usuario = models.OneToOneField(User,blank=True, null=True, on_delete=models.SET_NULL)
      class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
      def __str__(self):
        return u'{}'.format(self.municipio)

class provincia(models.Model):
      id= models.AutoField(primary_key=True)
      provincia= models.CharField(max_length=255, blank=True,choices=(('Artemisa','Artemisa'),('Habana','Habana'),('P. del Río','P. del Río'),('Mayabeque','Mayabeque'),('Matanzas','Matanzas'),('Cienfuegos','Cienfuegos'),('Villa Clara','Villa Clara'),
        ('Sancti Spíritus','Sancti Spíritus'),('Ciego de Ávila','Ciego de Ávila'),('Camagüey','Camagüey'),('Las Tunas','Las Tunas'),('Granma','Granma'),('Holguín','Holguín'),('Santiago de Cuba','Santiago de Cuba'),('Guantánamo','Guantánamo'),('Isla de la Juventud','Isla de la Juventud')))
      municipio= models.ManyToManyField(municipio,blank=True)
      usuario = models.OneToOneField(User,blank=True, null=True, on_delete=models.SET_NULL)
      class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
      def __str__(self):
        return u'{}'.format(self.provincia)







class pedido(models.Model):
      id= models.AutoField(primary_key=True)
      carnet=models.CharField(max_length=255)
      nombre=models.CharField(max_length=255)
      apellido1=models.CharField(max_length=255)
      apellido2=models.CharField(max_length=255)
      provincia= models.ForeignKey(provincia, null=True, blank=True, on_delete=models.CASCADE)
      municipio= models.ForeignKey(municipio, null=True, blank=True, on_delete=models.CASCADE)
      direccion= models.CharField(max_length=255)     
      cantidad= models.IntegerField(null=True,blank=True)#instructor=models.ForeignKey(instructor, null=True, blank=True, on_delete=models.CASCADE)
      sub_total= models.IntegerField(null=True,blank=True)
      date=models.DateField(auto_now_add=True,null=True,blank=True)
      servicio = models.ForeignKey(servicio, null=True, blank=True, on_delete=models.CASCADE)
      atendido=models.CharField(max_length=255, blank=True, null=True)

      class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        
      def __str__(self):
        return u'{}'.format(self.carnet)

