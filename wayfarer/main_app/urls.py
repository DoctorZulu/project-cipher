from django.urls import path
from . import views


urlpatterns = [
    path('', views.email, name='email'),
    path('home/', views.home, name='home'),
    path('barcode/', views.barcode, name='barcode'),
    path('barcode1/', views.barcode1, name='barcode1'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/login', views.login, name='login'),
    path('accounts/logout', views.logout, name='logout'),
    path('011100110111011101101111011100100110010001100110011010010111001101101000/', views.textscroll, name='textscroll'),
    path('profile/<int:profile_id>/post_create/', views.post_create, name='post_create'),
    path('<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('profile/<int:profile_id>/', views.profile, name='profile'),
    path('profile/<int:profile_id>/user_edit', views.user_edit, name='user_edit'),
    path('guess/', views.guess_handle, name='guess_handle'),
    path('do/not/go/gentle', views.success, name='success'),
    path('/a/b/y/s/s', views.abyss, name='abyss'),
    path('finalement', views.fin, name='fin')
]