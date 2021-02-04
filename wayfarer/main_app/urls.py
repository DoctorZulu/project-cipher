from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('email/', views.email, name='email'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/login', views.login, name='login'),
    path('accounts/logout', views.logout, name='logout'),
    path('011100110111011101101111011100100110010001100110011010010111001101101000/', views.textscroll, name='textscroll'),
]