from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [

    #Url para el controlador de vista de visualizer
    url(r'(?P<voting_id>.*)/$', views.view, name='view')
]
