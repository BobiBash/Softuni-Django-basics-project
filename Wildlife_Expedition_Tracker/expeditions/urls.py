from django.urls import path
from . import views

urlpatterns = [
    path("", views.expeditions_list, name="expeditions_list"),
    path("add-expedition/", views.add_expedition, name="add_expedition"),
    path("<int:pk>/", views.expedition_detail, name="expedition_detail"),
    path("<int:pk>/edit-expedition/", views.edit_expedition, name="edit_expedition"),
    path("<int:pk>/delete-expedition/", views.delete_expedition, name="delete_expedition"),
]