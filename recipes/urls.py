from django.urls import path

# from recipes.views import home
from recipes import views

urlpatterns = [
    path("", views.home),
    path("recipes/<int:id>/", views.recipes),
]
