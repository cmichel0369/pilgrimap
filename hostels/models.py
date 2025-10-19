from django.db import models
from django.contrib.auth.models import User

# Fonction pour récupérer une chambre par défaut (si elle existe)
def get_default_room():
    from .models import Room  # import local pour éviter une erreur circulaire
    return Room.objects.first().pk if Room.objects.exists() else None


class Hostel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    price_per_night = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=30.00  # ✅ valeur par défaut
    )

    def __str__(self):
        return self.name


class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    number = models.CharField(max_length=10, default="A1")  # ✅ valeur par défaut
    capacity = models.IntegerField(default=1)  # ✅ valeur par défaut

    def __str__(self):
        return f"Room {self.number} - {self.hostel.name}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, default=get_default_room)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.room}"


# ✅ Classe déplacée en dehors de Reservation (au bon niveau)
class WalletProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='walletprofile_hostel')
    wallet_address = models.CharField(max_length=42, unique=True)

    def __str__(self):
        return self.wallet_address