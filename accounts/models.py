from django.db import models
from django.contrib.auth.models import User

class WalletProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='walletprofile_account')
    wallet_address = models.CharField(max_length=42, unique=True)

    def __str__(self):
        return self.wallet_address
