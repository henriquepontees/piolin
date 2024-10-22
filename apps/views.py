from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *

def home(request):
  template = loader.get_template('pages/home.html')
  context = {
             'projetos': Projetos.objects.all(),
             'parceiros': Parceiros.objects.all(),
             'pix': ChavesPix.objects.all(),
             "eventos": Eventos.objects.all(),
            }
  return HttpResponse(template.render(context, request))

def noticias(request):
  all_noticias = Noticias.objects.order_by('-data')
  if(request.method == 'POST'):
        search = request.POST['search']
        all_noticias = Noticias.objects.filter(titulo__contains=search).order_by('-data') 
  paginator = Paginator(all_noticias, 6)  # Show 6 noticias per page.

  page_number = request.GET.get('page', 1)
  page_obj = paginator.get_page(page_number)
  current_page = page_obj.number
  context = {
        'noticias': page_obj,
        'previous_page': current_page - 1,
        'next_page': current_page + 1,
            }
  return render(request, 'pages/noticias.html', context)


def noticia(request, noticia_id):
  try:
    chosenNoticia = Noticias.objects.get(id=noticia_id)
    template = loader.get_template('pages/noticia.html')
    context = {'noticia': chosenNoticia,
               'noticias': Noticias.objects.order_by('-data')[:5]}
    return HttpResponse(template.render(context, request))
  except Noticias.DoesNotExist:
    return redirect('home')


def eventos(request):
  template = loader.get_template('pages/eventos.html')
  context = {
            }
  return HttpResponse(template.render(context, request))
