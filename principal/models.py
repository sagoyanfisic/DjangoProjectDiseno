#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
#clase a cambiar
class Bebida(models.Model):
	nombre = models.CharField(max_length=50)
	ingredientes = models.TextField()
	preparacion = models.TextField()

	def __unicode__(self):
		return self.nombre
#clase a camboar 
class Receta(models.Model):
	#Dato de la cadena , longitud
	titulo = models.CharField(max_length=100 , unique=True)
	#dato help_text para ayuda , no requerido
	ingredientes = models.TextField(help_text='Redacta los ingredientes')
	preparacion = models.TextField(verbose_name='Preparacion')
	#se almacenarán en la carpeta recetas, titulo: imagen
	imagen = models.ImageField(upload_to='recetas' , verbose_name='Imagen')
	#almacena la fehca y hora actual :D commmit :D ok no
	tiempo_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo
		

