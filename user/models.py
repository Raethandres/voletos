from django.db import models
from log.models import UserModel

class Voleto(models.Model):
	use=models.OneToOneField(UserModel, on_delete=models.CASCADE, null=True)
	serial=models.IntegerField()
	fecha=models.DateField()
	ubicacion=models.CharField(max_length=40)

class Evento(models.Model):
	postion=(('V','VIP'),('A','alto'),('M','medio'),('P','platino'))
	name=models.CharField(max_length=40)
	posi=models.CharField(max_length=1,choices=postion)
	voletos=models.ManyToManyField(Voleto,null=True)


	
		

# Create your models here.
