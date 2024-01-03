from django.contrib import admin
from django.urls import path
from base import views
from django.conf.urls import include

urlpatterns = [ 
    path('',views.homeindex, name='home'),
   
   
]