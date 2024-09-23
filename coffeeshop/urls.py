from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about', views.about, name='about'),  # Sesuaikan dengan string URL
    path('menu', views.menu, name='menu'), 
]