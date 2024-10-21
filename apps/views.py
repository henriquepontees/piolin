from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from .models import *

def home(request):
  template = loader.get_template('pages/home.html')
  context = {
             'projetos': Projetos.objects.all(),
             'parceiros': Parceiros.objects.all(),
             'pix': ChavesPix.objects.all(),
            }
  return HttpResponse(template.render(context, request))

def noticias(request):
  template = loader.get_template('pages/noticias.html')
  context = {
            }
  return HttpResponse(template.render(context, request))