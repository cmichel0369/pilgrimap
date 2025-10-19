from django.urls import path
from . import views

urlpatterns = [
    path('wallet-login/', views.wallet_login_view, name='wallet_login'),
    path('', views.home, name='home'),
    path('reservation/', views.reservation_form, name='reservation'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
]