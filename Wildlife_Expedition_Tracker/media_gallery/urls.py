from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_gallery, name="display_gallery"),
    path("<slug:slug>/", views.image_detail, name="image_detail"),
]