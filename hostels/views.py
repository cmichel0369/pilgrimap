from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Hostel, Room, Booking
from .forms import HostelForm, RoomForm, BookingForm

def list_hostels(request):
    hostels = Hostel.objects.all()
    return render(request, 'hostels/hostel_list.html', {'hostels': hostels})


def hostel_detail(request, hostel_id):
    hostel = get_object_or_404(Hostel, id=hostel_id)
    rooms = Room.objects.filter(hostel=hostel)
    return render(request, 'hostels/hostel_detail.html', {'hostel': hostel, 'rooms': rooms})


@login_required
def add_hostel(request):
    if request.method == 'POST':
        form = HostelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_hostels')
    else:
        form = HostelForm()
    return render(request, 'hostels/add_hostel.html', {'form': form})


@login_required
def edit_hostel(request, hostel_id):
    hostel = get_object_or_404(Hostel, id=hostel_id)
    if request.method == 'POST':
        form = HostelForm(request.POST, request.FILES, instance=hostel)
        if form.is_valid():
            form.save()
            return redirect('hostel_detail', hostel_id=hostel.id)
    else:
        form = HostelForm(instance=hostel)
    return render(request, 'hostels/edit_hostel.html', {'form': form, 'hostel': hostel})


@login_required
def delete_hostel(request, hostel_id):
    hostel = get_object_or_404(Hostel, id=hostel_id)
    hostel.delete()
    return redirect('list_hostels')


@login_required
def add_room(request, hostel_id):
    hostel = get_object_or_404(Hostel, id=hostel_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.hostel = hostel
            room.save()
            return redirect('hostel_detail', hostel_id=hostel.id)
    else:
        form = RoomForm()
    return render(request, 'hostels/add_room.html', {'form': form, 'hostel': hostel})


@login_required
def add_booking(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.user = request.user
            booking.save()
            room.is_available = False
            room.save()
            return redirect('hostel_detail', hostel_id=room.hostel.id)
    else:
        form = BookingForm()
    return render(request, 'hostels/add_booking.html', {'form': form, 'room': room})

def list_rooms(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'hostels/room_list.html', {'rooms': rooms})
