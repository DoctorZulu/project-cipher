from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('email/', views.email, name='email'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/login', views.login, name='login'),
    path('accounts/logout', views.logout, name='logout'),
]