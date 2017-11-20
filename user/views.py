from django.shortcuts import render
from django.views import View
from .models import Voleto,Evento
from django.http import JsonResponse
from log.decorator import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class admin(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(admin, self).dispatch(request, *args, **kwargs)
	
	def get(self,request):
		vole=Voleto.objects.all()
		vole.order_by('fecha')
		vec=[(x.use.all()[0].user.first_name,x.use.all()[0].user.last_name,x.use.all()[0].id,x.use.all()[0].tipo,x.use.all()[0].cedula,x.evento_set.all()[0].name,x.ubicacion)for x in vole]
		return JsonResponse({"status":True,"row":vec})

	
	def post(self,request):
		eve=Evento(name=request.POST["evento"])
		eve.save()
		return JsonResponse({"status":True})

	def put(self,request):
		pass

	def delete(self,request):
		vole=Voleto.objects.get(id=request.DELETE["id"])
		vole.delete()
		return JsonResponse({"status":True})

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
	if request.method=="GET":
		print(request.GET["ff"])
		x=Voleto.objects.get(id=request.GET["id"])
		vec=(x.use.all()[0].user.first_name,x.use.all()[0].user.last_name,x.use.all()[0].genero,x.use.all()[0].telefono,x.use.all()[0].email,x.use.all()[0].direccion,x.use.all()[0].cedula,x.evento_set.all()[0].name,x.ubicacion)
		return JsonResponse({"status":True,"vec":vec})

def getEvento(request):
	pass


# Create your views here.
