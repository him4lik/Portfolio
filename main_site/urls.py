from django.urls import path
from main_site import views 

urlpatterns=[
	path('', views.home, name='home'),
	
]