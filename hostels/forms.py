from django import forms
from .models import Hostel, Room

class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ['name', 'address', 'city', 'description']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['hostel', 'name', 'capacity', 'price', 'is_available']
