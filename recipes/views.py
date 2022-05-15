from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(
        request,
        "recipes/home.html",
        context={
            "name": "Thiago José",
        },
    )


def sobre(request):
    return HttpResponse("recipes/Sobre")


def contato(request):
    return HttpResponse("recipes/Contato")
