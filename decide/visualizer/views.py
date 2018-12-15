from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404
from django.shortcuts import render

from base import mods

#Controlador vista visualizer
def view(request,voting_id):
    #Asignacion de votacion con id voting_id, tomado de la url
    voting = mods.get('voting', id = voting_id)

    #Renderizacion de la vista con template 'visualizer/visualizer.html
    #y variable voting
    return render(request, 'visualizer/visualizer.html',
                  {'voting': voting[0]})

