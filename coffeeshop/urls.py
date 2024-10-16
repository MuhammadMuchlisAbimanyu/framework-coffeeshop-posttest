from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about', views.about, name='about'),  # Sesuaikan dengan string URL
    path('menu', views.CRUD_Coffee, name='CoffeeList'), 
    path('Coffees/add_coffees', views.add_coffee, name='add_coffee'),
    path('Coffees/<int:coffee_id>/update', views.update_coffee, name='coffee_update'),
    path('coffee/delete/<int:coffee_id>/', views.coffee_delete, name='coffee_delete'),
]