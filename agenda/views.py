from django.shortcuts import render,redirect
from .models import agenda


def home(request):
    return render(request,"home.html")

def agendar(request):
    agendas=agenda.objects.all()
    return render(request,"agenda.html",{"agendas":agendas})
    
def salvar(request):
    
    nome= request.POST.get('nome')
    dia = request.POST.get('dia')
    hora = request.POST.get('hora')
    servico = request.POST.get('servico')
    agenda.objects.create(nome=nome,dia=dia,hora=hora,servico=servico)
    agendas = agenda.objects.all()
    return redirect(agendar)

def excluir(request,id):
    agendas=agenda.objects.get(id=id)
    agendas.delete()
    return redirect(agendar)