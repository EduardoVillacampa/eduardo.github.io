from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms

# Create your views here

def index(request):
	return render(request, "web/index.html")

def quiensomos_view(request):
	return render(request, "web/quiensomos.html")
