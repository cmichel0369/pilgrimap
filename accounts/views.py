from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import WalletProfile
import json

# Vue pour afficher la page avec le bouton MetaMask
def wallet_login_page(request):
    return render(request, 'wallet_login.html')

# Vue pour tester MetaMask
def test_metamask(request):
    return render(request, 'test.html')

# Vue pour traiter la connexion depuis MetaMask
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
            return JsonResponse({'message': f'Connexion réussie ! Bienvenue {user.username}'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'message': 'Méthode non autorisée'}, status=405)