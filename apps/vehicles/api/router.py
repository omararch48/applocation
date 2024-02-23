from django.urls import path
from . import views


urlpatterns = [
    path('get_vehicle/<int:pk>/', views.get_vehicle, name='get_vehicle'),
    path('create_vehicle/', views.create_vehicle, name='create_vehicle'),
    path('get_all_vehicles/', views.get_all_vehicles, name='get_all_vehicles'),
    path(
        'update_vehicle/<int:pk>/', views.update_vehicle, name='update_vehicle'
    ),
    path(
        'delete_vehicle/<int:pk>/', views.delete_vehicle, name='delete_vehicle'
    ),
]