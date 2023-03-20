
from django.urls import path
from .views import inicio, products, exit, quiensomos, noticia1, noticia2, noticia3, servicios, formulario, registro_usuario
from . import views

urlpatterns = [
    path('', inicio, name='inicio'),
    path('products/', products, name='products'),
    path('logout/', exit, name='exit'),
    path("quiensomos.html", quiensomos, name="quiensomos"),
    path("inicio.html", inicio, name="inicio"),
    path("formulario.html", formulario, name="formulario"),
    path("servicios.html", servicios, name="servicios"),
    path("noticia1.html", noticia1, name="noticia1"),
    path("noticia2.html", noticia2, name="noticia2"),
    path("noticia3.html", noticia3, name="noticia3"),
    path("registro/", registro_usuario, name="registro_usuario")
]