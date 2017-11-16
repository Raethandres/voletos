from django.db import models
from log.models import UserModel

class Voleto(object):
	use=models.OneToOneField(UserModel, on_delete=models.CASCADE, null=True)
	serial=models.IntegerField()
	fecha
	ubicacion=models.CharField(max_length=40)

class Evento(object):
	postion=(('V','VIP'),('A','alto'),('M','medio'),('P','platino'))
	voletos=models.ManyToManyField(Voleto,null=True)
	name=models.CharField(max_length=40)
	posi=models.CharField(max_length=1,choices=postion)


	
		

# Create your models here.
