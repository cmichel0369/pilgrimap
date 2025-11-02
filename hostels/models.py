from django.db import models
from django.contrib.auth.models import User

class Hostel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='hostels_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='rooms_photos/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.hostel.name})"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.room.name}"
