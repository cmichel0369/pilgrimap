from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Hostel, Room, Reservation

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Requis.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ['name', 'address', 'description', 'price_per_night']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'capacity', 'hostel']  # ✅ Le champ "number" est ici


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'check_in', 'check_out']