from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('search/', views.search_view, name='search'),
    path("about/", views.about, name="about"),
    path('gallery/', views.media_gallery, name='media_gallery'),
]