from django import forms
from .models import Hostel, Room, Booking

class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ['name', 'description', 'city', 'address', 'photo']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description', 'price_per_night', 'capacity', 'photo', 'is_available']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out']
