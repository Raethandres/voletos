from django.db import models
from log.models import UserModel

class Voleto(models.Model):
	postion=(('V','VIP'),('A','alto'),('M','medio'),('P','platino'))
	use=models.ManyToManyField(UserModel, null=True)
	serial=models.IntegerField()
	fecha=models.DateField()
	ubicacion=models.CharField(max_length=40)
	posi=models.CharField(max_length=1,choices=postion)

	def __str__(self):
		return str(self.use)

class Evento(models.Model):
	name=models.CharField(max_length=40)
	voleto=models.ManyToManyField(Voleto,null=True)

	def __str__(self):
		return str(self.use)


	
		

# Create your models here.
