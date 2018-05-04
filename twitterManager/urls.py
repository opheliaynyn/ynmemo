from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import django.contrib.auth.views

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('login/',
         django.contrib.auth.views.login,
         {
             'template_name': 'twitterManager/login.html',
         },
         name='login'),
    path('logout/',
         django.contrib.auth.views.logout,
         {
             'template_name': 'twitterManager/logout.html',
         },
         name='logout'),
]