from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms

# Create your views here.

class FormularioUsuario (forms.Form):
	nombres = forms.CharField(label="Nuevo usuario")
	rango = forms.IntegerField(label="Registrarse como:")

def index(request):
	
	if "listaUsuarios" not in request.session:
		request.session["listaUsuarios"] = []
	return render(request, "nombres/index.html", {
		"nombres": request.session["listaUsuarios"]
	})

def add(request):
	if request.method == "POST":
		formulario = Formulariousuario(request.POST)
		if formulario.is_valid():
			tarea = formulario.cleaned_data["nombres"]
			request.session["listaUsuarios"] += [tarea]
			return HttpResponseRedirect(reverse("nombres:index"))
		else:
			return render(request, "nombres/add.html", {
				"form": formulario
			})
	else:
		return render(request, "nombres/add.html", {
			"form":FormularioUsuario()
		})
