from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def actions(request):
    return render(request, "actions.html")