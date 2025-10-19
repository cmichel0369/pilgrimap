from django.urls import path
from . import views

urlpatterns = [
    path('wallet-login/', views.wallet_login, name='wallet_login'),
    path('login-wallet/', views.wallet_login_page, name='wallet_login_page'),
    path('test-metamask/', views.test_metamask, name='test_metamask'),
]