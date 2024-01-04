from django.contrib import admin
from django.urls import path
from base import views
from django.conf.urls import include

urlpatterns = [ 
    path('',views.homeindex, name='home'),
    path('tafsir',views.tafsir, name='tafsir'),
    path('about',views.about, name='about'),
    path('publications',views.publications, name='publications'),
    path('gallery',views.gallery, name='gallery'),
    path('poeme',views.poeme, name='poeme'),
]