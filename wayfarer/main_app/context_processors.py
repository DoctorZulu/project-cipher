from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Post


def add_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=user)
        return{
            'profile': profile,
            'profiles': Profile.objects.all()
            
        }
    else:
        return{
            
        }
        
def add_posts(request):
    posts = Post.objects.all()
    return{
        'posts' : posts
    }


