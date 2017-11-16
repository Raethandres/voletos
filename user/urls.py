from django.conf.urls import include, url
from .views import * 

urlpatterns= [
		# url(r'^accounts/', include('django.contrib.auth.urls')),
		url(r'^admin/$', admin.as_view(),name="admin"),
		url(r'^user/$',user.as_view(),name="user"),
		url(r'^voleto/$', views.getVoleto,name="voleto"),
		url(r'^evento/$', views.getEvento,name="evento"),


	]