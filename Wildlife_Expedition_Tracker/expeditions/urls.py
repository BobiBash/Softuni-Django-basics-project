from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.expeditions_list, name="expeditions_list"),
    path("add-expedition/", views.add_expedition, name="add_expedition"),
    path("<slug:slug>/", views.expedition_detail, name="expedition_detail"),
    path("<slug:slug>/edit-expedition/", views.edit_expedition, name="edit_expedition"),
    path("<slug:slug>/delete-expedition/", views.delete_expedition, name="delete_expedition"),
    path("<slug:slug>/", include('sightings.urls'))
]