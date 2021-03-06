from django.shortcuts import render, get_object_or_404
from models import Professor, Modulo, Aula

def index(request):
    return render(request, "index.html")

def show_professor(request):
    profs = Professor.objects.all()
    return render(request, "professor.html",
    {
        'professores': profs,
    })

def show_modules(request, pk):
    modules = Modulo.objects.filter(video__professor=pk)
    return render(request, "module.html",
    {
        'modules': modules,
    })

def show_classes(request, pk):
    classes = Aula.objects.filter(modulo=pk)
    return render(request, "class.html",
    {
        'classes': classes,
    })
