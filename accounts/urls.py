from django.urls import path
from . import views

urlpatterns = [
    path('wallet-login/', views.wallet_login, name='wallet_login'),        # POST (MetaMask)
    path('login-wallet/', views.wallet_login_page, name='wallet_login_page'),  # Affichage HTML
     # ... autres routes ...
    path('test-metamask/', views.test_metamask, name='test_metamask'),
]