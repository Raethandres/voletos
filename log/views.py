from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .decorator import login,log,logout
import json
from .models import UserModel
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse


@csrf_exempt
def logi(request):
	print("ss")
	
	if request.method == "POST":
		
		print(request.POST)
		rq=request.POST

		if rq:
			try:
				user=User.objects.get(username=rq['uname'])
				print(user,"s")
				st=authenticate(username=rq['uname'],password=rq['pass'])
				print(st,"w")
				if st is not None:
					if st.is_active:
						login(user)
						print(user.usermodel.tipo,"j")
						return JsonResponse({'status':True,'row':user.usermodel.tipo})
					else:
						return JsonResponse({'status':False,'st':'not activate'})

				else:
					print(st,"f")					
					lin=False
					return JsonResponse({'status':False,'st':'notpaswo'})
			except Exception as e:
				lin=False
				print(e)
				return JsonResponse({'status':False,'st':'notfound'})
	# print(request)
	# form=LoginForm()
	return JsonResponse({'status':False})


# Create your views here.


def falla(request):
	return JsonResponse({'status':True})

@csrf_exempt
def logup(request):
	print("lup")
	if request.method=='POST':
		try:
			print(request.POST)
			uss=request.POST['username']
			print(uss)
			user= User(username=request.POST['username'], email="wq@f.com")
			print("ww")
			user.set_password(request.POST['pass'])
			user.first_name=request.POST.get('nombre')
			user.last_name=request.POST.get('apellido')
			user.save()
			use=UserModel()
			use.cedula=request.POST.get('cedula')
			use.genero=request.POST.get('sexo')
			use.direccion=request.POST.get('direccion')
			use.email=request.POST.get('email')
			use.telefono=request.POST.get('telefono')
			use.tipo=0
			use.user=user
			use.save()
			return JsonResponse({'status':True})
		except Exception as e:
			print(e)
			return JsonResponse({'status':False,'tipe':e})
	return JsonResponse({'status':False})


@csrf_exempt
def logot(request):
	if request.method=="GET":
		print("wswsp")
		logout()
		return JsonResponse({'status':True})
	else:
		return JsonResponse({'status':False})
