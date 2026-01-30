from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_expedition, name="add_expedition"),
]