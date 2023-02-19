from django.urls import path, include
from . import views

app_name = "web"

urlpatterns = [
        path("", views.index, name="index"),
        path('index.html', views.index, name="index"),
        path("quiensomos.html", views.quiensomos_view, name="quiensomos.html"),
        path("servicios.html", views.servicios_view, name="servicios.html"),
        path("clientes.html", views.clientes_view, name="clientes.html"),
        path("noticia1.html", views.noticia1_view, name="noticia1.html"),
        path("noticia2.html", views.noticia2_view, name="noticia2.html"),
        path("noticia3.html", views.noticia3_view, name="noticia3.html"),
        path('accounts/', include('django.contrib.auth.urls'))
]
