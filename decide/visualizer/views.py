from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from decide.static.fusioncharts import FusionCharts

from base import mods

#Controlador vista visualizer
def view(request,voting_id):
    #Asignacion de votacion con id voting_id, tomado de la url

    voting = mods.get('voting', params={'id' : voting_id})
    carga = True
    totalvotes = 0
    aux = []
    carga = False
    try:
        for option in voting[0]["postproc"] :
            aux.append({"label" : ""+option["option"], "value": ""+str(option["votes"])})
            totalvotes = totalvotes + option["votes"]

        dataSource = {"chart": {
                "caption": "Porcentaje de Votos",
                "subCaption" : ""+voting[0]["name"]+" Votos",
                "showValues":"1",
                "showPercentInTooltip" : "0",
                "numberPrefix" : "$",
                "enableMultiSlicing":"1",
                "theme": "fusion"
            },
            "data": aux}

        pie3d = FusionCharts("pie3d", "ex2" , "100%", "400", "chart-1", "json", dataSource)
        carga = True
    except:
        print(carga)
        return render(request, 'visualizer/visualizer.html',
                  {'carga':carga})
    #Renderizacion de la vista con template 'visualizer/visualizer.html
    #y variable voting
    return render(request, 'visualizer/visualizer.html',
                  {'voting': voting[0],'output' : pie3d.render(), 'chartTitle': 'Pie 3D Chart', 'totalvotes': totalvotes, 'carga':carga})

