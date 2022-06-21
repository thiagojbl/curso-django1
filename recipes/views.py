# from django.http import Http404

import os

from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.pagination import make_pagination

from recipes.models import Recipe

# from utils.recipes.factory import make_recipe

#
# for i in range(10): r.id = None; r.save()
# for i, recipe in enumerate(r): recipe.title =
# recipe.title+str(i+1); recipe.save()

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    messages.success(request, 'Olá, uma mensagem de sucesso!')
    messages.warning(request, 'Olá, uma mensagem de sucesso!')
    messages.error(request, 'Olá, uma mensagem de sucesso!')

    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": page_obj,
            "pagination_range": pagination_range,
        },
    )


def category(request, category_id):
    print("chegou: ", category_id)

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by("-id")
    )

    # if not recipes:
    #     raise Http404("Category não encontrada (^_^)")
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    return render(
        request,
        "recipes/pages/category.html",
        context={
            "recipes": page_obj,
            'pagination_range': pagination_range,
            "title": f"{recipes[0].category.name} - Category |",
        },
    )


# Create your views here.
def recipes(request, id):
    recipe = get_object_or_404(
        Recipe,
        pk=id,
        is_published=True,
    )
    return render(
        request,
        "recipes/pages/recipes-view.html",
        context={
            "recipe": recipe,
            "is_detail_page": True,
        },
    )


def search(request):
    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    )
    # recipes = recipes.filter(is_published=True)
    recipes = recipes.order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'search for "{search_term}"',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_quey': f'&q={search_term}',
    })
