from django.shortcuts import render


# Create your views here.
def home(request):
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "name": "Thiago José",
        },
    )


# Create your views here.
def recipes(request, id):
    return render(
        request,
        "recipes/pages/recipes-view.html",
        context={
            "name": "Thiago José",
        },
    )
