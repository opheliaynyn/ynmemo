from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
]