from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("robustness", views.robustness, name="robustness"),
    path("evasion", views.evasion, name="evasion"),
]