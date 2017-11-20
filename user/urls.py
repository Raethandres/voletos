from django.conf.urls import include, url
from . import views
from .views import *

urlpatterns= [
		# url(r'^accounts/', include('django.contrib.auth.urls')),
		url(r'^adminis/$', admin.as_view(),name="admin"),
		url(r'^perfil/$', perfil.as_view(),name="perfil"),
		url(r'^user/$',user.as_view(),name="user"),
		url(r'^voleto/$', views.getVoleto,name="voleto"),
		url(r'^evento/$', views.getEvento,name="evento"),


	]