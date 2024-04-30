from django.urls import path, include
from service import views

urlpatterns = [
    path("", include("service.urls"))
]

handler404 = views.page_not_found