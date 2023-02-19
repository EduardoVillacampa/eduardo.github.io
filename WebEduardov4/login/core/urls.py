
from django.urls import path
from .views import inicio, products, exit
from . import views

urlpatterns = [
    path('', inicio, name='inicio'),
    path('products/', products, name='products'),
    path('logout/', exit, name='exit'),
    path("quiensomos.html", views.quiensomos_view, name="quiensomos.html"),
    path("inicio.html", inicio, name="inicio.html"),
    path("servicios.html", views.servicios_view, name="servicios.html"),
    path("noticia1.html", views.noticia1_view, name="noticia1.html"),
    path("noticia2.html", views.noticia2_view, name="noticia2.html"),
    path("noticia3.html", views.noticia3_view, name="noticia3.html")
]