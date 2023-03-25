from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("category/<slug>/", category, name="category"),
    path("view/<int:pk>/", view, name="view"),






]