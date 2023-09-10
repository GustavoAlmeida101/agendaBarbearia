from django.contrib import admin
from django.urls import path
from .views import home,agendar,salvar,excluir

urlpatterns = [
    path('', home,name='home'),
    path('agenda/', agendar,name='agendar'),
    path('salvar/', salvar,name='salvar'),
    path('excluir/<int:id>',excluir,name='excluir')
    
]