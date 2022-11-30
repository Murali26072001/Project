from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views
urlpatterns=[
	path("login",views.login),
	path("add",views.Staff.Add_Staff),
	
	
]

#path('', image_request, name = "image-request"),
