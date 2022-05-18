from django.shortcuts import render
from utils.recipes.factory import make_recipe


# Create your views here.
def home(request):
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": [make_recipe() for _ in range(10)],
        },
    )


# Create your views here.
def recipes(request, id):
    return render(
        request,
        # "base_templates/global/base.html",
        "recipes/pages/recipes-view.html",
        context={
            "recipe": make_recipe(),
            "is_detail_page": True,
        },
    )
