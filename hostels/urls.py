from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_hostels, name='list_hostels'),
    path('add/', views.add_hostel, name='add_hostel'),
    path('<int:hostel_id>/', views.hostel_detail, name='hostel_detail'),
    path('<int:hostel_id>/edit/', views.edit_hostel, name='edit_hostel'),
    path('<int:hostel_id>/delete/', views.delete_hostel, name='delete_hostel'),
    path('<int:hostel_id>/rooms/add/', views.add_room, name='add_room'),
    path('rooms/<int:room_id>/book/', views.add_booking, name='add_booking'),
    path('rooms/', views.list_rooms, name='list_rooms'),
]
