from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import WalletProfile  # 👈 à adapter selon le nom de ton app

@csrf_exempt
def wallet_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            wallet_address = data.get('wallet_address', '').lower()

            if not wallet_address:
                return JsonResponse({'error': 'Adresse du wallet manquante.'}, status=400)

            profile, created = WalletProfile.objects.get_or_create(wallet_address=wallet_address)

            if created:
                user = User.objects.create(username=wallet_address[:30])
                profile.user = user
                profile.save()
            else:
                user = profile.user

            login(request, user)
            return JsonResponse({'message': 'Connexion réussie', 'username': user.username})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'message': 'Méthode non autorisée'}, status=405)
