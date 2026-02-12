from django.urls import path
from . import views

urlpatterns = [
    path('sighting-list/', views.sighting_list, name='sighting_list'),
    path('sighting/detail/<int:pk>', views.sighting_detail, name='sighting_detail'),
    path('add-sighting/', views.add_sighting, name='add_sighting'),
    path('edit-sighting/<int:pk>/', views.edit_sighting, name='edit_sighting'),
    path('sighting/delete/<int:pk>/', views.delete_sighting, name='delete_sighting'),
]