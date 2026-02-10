from django.urls import path
from . import views


urlpatterns = [
    path('', views.animals_list, name='animals_list'),
    path("<slug:slug>/", views.animal_detail, name='animal_detail')
]