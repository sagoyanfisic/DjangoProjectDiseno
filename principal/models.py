from django.db import models

class Bebida(models.model):
	nombre = models.CharField(max_length=50)
	ingredientes = models.TextField()
	preparacion = models.TextField()
	

	def __unicode__(self):
		return self.nombre
