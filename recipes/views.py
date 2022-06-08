# from django.http import Http404

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe

# from utils.recipes.factory import make_recipe

#
# for i in range(10): r.id = None; r.save()
# for i, recipe in enumerate(r): recipe.title =
# recipe.title+str(i+1); recipe.save()


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")

    current_page = request.GET.get('page', 1)
    paginator = Paginator(recipes, 9)
    page_obj = paginator.get_page(current_page)
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": page_obj,
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
    return render(
        request,
        "recipes/pages/category.html",
        context={
            "recipes": recipes,
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

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'search for "{search_term}"',
        'search_term': search_term,
        'recipes': recipes,
    })
