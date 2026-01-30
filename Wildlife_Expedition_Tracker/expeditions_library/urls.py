from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_expeditions, name="display_expeditions"),
    path("edit/<int:pk>/", views.edit_expedition, name="edit_expedition"),
    path("delete/<int:pk>/", views.delete_expedition, name="delete_expedition"),
]