from django.db import models
from django.contrib.auth.models import User

class UserModel(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	log=models.BooleanField(default=False)
	tipo=models.IntegerField()
	cedula=models.IntegerField()
	genero=models.CharField(max_length=1)
	direccion=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	telefono=models.IntegerField()

	def __str__(self):
		return str(self.user)


# Create your models here.
