from django.urls import path

from .views import *

urlpatterns = [
    path("", Jose.as_view()),
]
