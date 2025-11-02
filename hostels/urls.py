from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Hostels
    path('hostels/', views.list_hostels, name='list_hostels'),
    path('hostels/add/', views.add_hostel, name='add_hostel'),
    path('hostels/<int:hostel_id>/', views.detail_hostel, name='detail_hostel'),
    path('hostels/<int:hostel_id>/delete/', views.delete_hostel, name='delete_hostel'),

    # Rooms
    path('rooms/', views.list_rooms, name='list_rooms'),
    path('rooms/add/', views.add_room, name='add_room'),
    path('rooms/<int:room_id>/book/', views.book_room, name='book_room'),

    # Dashboard
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
]
