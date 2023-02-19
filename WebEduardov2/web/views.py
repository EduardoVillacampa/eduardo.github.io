from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms

# Create your views here

def index(request):
	return render(request, "web/index.html")

def quiensomos_view(request):
	return render(request, "web/quiensomos.html")

def servicios_view(request):
	return render(request, "web/servicios.html")

def clientes_view(request):
	return render(request, "web/clientes.html")

def noticia1_view(request):
	return render(request, "web/noticia1.html")

def noticia2_view(request):
	return render(request, "web/noticia2.html")

def noticia3_view(request):
	return render(request, "web/noticia3.html")