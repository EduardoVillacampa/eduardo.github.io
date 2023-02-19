from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

@login_required
def products(request):
    return render(request, 'core/products.html')

def exit(request):
    logout(request)
    return redirect('inicio')

def quiensomos_view(request):
	return render(request, "core/quiensomos.html")

def servicios_view(request):
	return render(request, "core/servicios.html")

def noticia1_view(request):
	return render(request, "core/noticia1.html")

def noticia2_view(request):
	return render(request, "core/noticia2.html")

def noticia3_view(request):
	return render(request, "core/noticia3.html")

