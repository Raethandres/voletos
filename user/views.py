from django.shortcuts import render
from django.views import View
from .models import Voleto,Evento
from django.http import JsonResponse

class admin(View):
	
	def get(self,request):
		vole=Voleto.objects.all()
		vole.order_by('name')
		vec=[(i.use.name,i.serial,i.fecha,i.note,i.ubicacion)for i in vole]
		return JsonResponse({"status":True,"work":vec})


	def post(self,request):
		pass

	def put(self,request):
		pass

	def delete(self,request):
		pass
		
class user(View):
	
	def get(self,request):
		pass

	def post(self,request):
		pass

	def put(self,request):
		pass

	def delete(self,request):
		pass
		

def getVoleto(request):
	pass

def getEvento(request):
	pass


# Create your views here.
