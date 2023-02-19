from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
        path('', views.index, name="index"),
        path("quiensomos", views.quiensomos_view, name="quiensomos")

]
