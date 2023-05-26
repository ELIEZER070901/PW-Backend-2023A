#Agregar bibliotec administradora de rutas
from django.urls import path
#Importando vistas
from . import views 

#Declarando rutas validas
urlpatterns = [
    path("", views.index, name="index"),
    path("author/", views.author, name="author"),
]