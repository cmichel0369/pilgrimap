from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Hostel, Room, Booking
from .forms import HostelForm, RoomForm

def index(request):
    return render(request, 'hostels/index.html')

# ---- Hostel views ----
def list_hostels(request):
    hostels = Hostel.objects.all()
    return render(request, 'hostels/hostel_list.html', {'hostels': hostels})


@login_required
def add_hostel(request):
    if request.method == 'POST':
        form = HostelForm(request.POST)
        if form.is_valid():
            hostel = form.save(commit=False)
            hostel.owner = request.user
            hostel.save()
            return redirect('list_hostels')
    else:
        form = HostelForm()
    return render(request, 'hostels/hostel_form.html', {'form': form})


def detail_hostel(request, hostel_id):
    hostel = get_object_or_404(Hostel, id=hostel_id)
    rooms = hostel.rooms.all()
    return render(request, 'hostels/hostel_detail.html', {'hostel': hostel, 'rooms': rooms})


@login_required
def delete_hostel(request, hostel_id):
    hostel = get_object_or_404(Hostel, id=hostel_id, owner=request.user)
    hostel.delete()
    return redirect('list_hostels')


# ---- Room views ----
def list_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'hostels/room_list.html', {'rooms': rooms})


@login_required
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_rooms')
    else:
        form = RoomForm()
    return render(request, 'hostels/room_form.html', {'form': form})


@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        Booking.objects.create(room=room, user=request.user)
        room.is_available = False
        room.save()
        return redirect('user_dashboard')
    return render(request, 'hostels/book_room.html', {'room': room})


@login_required
def user_dashboard(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'hostels/dashboard.html', {'bookings': bookings})
