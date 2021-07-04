from django.urls import path

from .views import * # this is the views.py file within this directory

urlpatterns = [
    path("", index, name="index_page"),
    path("show/<uuid:id>", show, name="show_page"),
    path("random", add_random, name="add_random"),
    path("search/", search, name='search')
]