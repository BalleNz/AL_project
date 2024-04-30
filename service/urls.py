from django.urls import path
from service import views

urlpatterns = [
    path("", views.index, name="main"),
    path("search-el", views.search_element, name="search_element"),
    path("all-elements", views.all_elements, name="all_elements")
]