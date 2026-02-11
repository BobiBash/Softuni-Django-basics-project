from django.urls import path
from . import views

urlpatterns = [
    path('<slug:expedition_slug>/sighting/detail/<int:pk>', views.sighting_detail, name='sighting_detail'),
    path('<slug:expedition_slug>/sighting/add/', views.add_sighting, name='add_sighting'),
    path('<slug:expedition_slug>/sighting/edit/<int:pk>/', views.edit_sighting, name='edit_sighting'),
    path('<slug:expedition_slug>/sighting/delete/<int:pk>/', views.delete_sighting, name='delete_sighting'),
]