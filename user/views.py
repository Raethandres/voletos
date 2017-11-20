from django.shortcuts import render
from django.views import View
from .models import Voleto,Evento
from django.http import JsonResponse
from log.decorator import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class perfil(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(perfil, self).dispatch(request, *args, **kwargs)
	
	def get(self,request):
		use=log()
		vec=(use.user.first_name,use.user.last_name,use.cedula,use.genero,use.direccion,use.email,use.telefono,use.user.username,use.user.password)
		return JsonResponse({"status":True,"row":vec})
	def post(self,request):
		pass

class admin(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(admin, self).dispatch(request, *args, **kwargs)
	
	def get(self,request):
		if request.GET.get("delete"):
			vole=Voleto.objects.get(id=request.GET["delete"])
			vole.delete()
			return JsonResponse({"status":True})

		vole=Voleto.objects.all()
		vole.order_by('fecha')
		vec=[(x.use.all()[0].user.first_name,x.use.all()[0].user.last_name,x.use.all()[0].id,x.use.all()[0].tipo,x.use.all()[0].cedula,x.evento_set.all()[0].name,x.ubicacion)for x in vole]
		return JsonResponse({"status":True,"row":vec})

	
	def post(self,request):
		if request.GET.get("delete"):
			pass
		eve=Evento(name=request.POST["evento"])
		eve.save()
		return JsonResponse({"status":True})





class user(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(user, self).dispatch(request, *args, **kwargs)

	def get(self,request):
		vec=[(log().user.first_name,i.serial,i.fecha,i.id,i.ubicacion)for i in log().voleto_set.all()]
		return JsonResponse({"status":True,"work":vec})

	def post(self,request):
		pass


def getVoleto(request):
	print("ww")
	if request.method=="GET":
		print(request.GET)
		x=Voleto.objects.get(id=request.GET.get('id'))
		vec=(x.use.all()[0].user.first_name,x.use.all()[0].user.last_name,x.use.all()[0].genero,x.use.all()[0].telefono,x.use.all()[0].email,x.use.all()[0].direccion,x.use.all()[0].cedula,x.evento_set.all()[0].name,x.ubicacion)
		return JsonResponse({"status":True,"vec":vec})

def getEvento(request):
	if request.method=="GET":
		x=Evento.objects.all()
		vec=[(i.name)for i in x]
		return JsonResponse({"status":True,"vec":vec})

# Create your views here.
