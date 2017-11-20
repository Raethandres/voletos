from django.shortcuts import render
from django.views import View
from .models import Voleto,Evento
from django.http import JsonResponse
from log.decorator import *

class admin(View):
	
	def get(self,request):
		vole=log()
		vol=vole.voletos_set.all()
		# print(log())
		vec=[(vole.name,i.serial,i.fecha,i.note,i.ubicacion)for i in vol]
		return JsonResponse({"status":True,"work":vec})


	def post(self,request):
		eve=Evento(name=request.POST["name"])
		eve.save()


	def put(self,request):
		pass

	def delete(self,request):
		vole=Voleto.objects.get(request.DELETE["id"])
		vole.delete()
		
class user(View):
	
	def get(self,request):
		print(log())
		vole=Voleto.objects.get(use=log())
		vole.order_by('name')
		vec=[(i.voleto_set.name,i.serial,i.fecha,i.note,i.ubicacion)for i in vole]
		return JsonResponse({"status":True,"work":vec})

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
