from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Puzzle

def add_puzzles(request):
    puzzles = Puzzle.objects.all()
    return{
        'puzzles' : puzzles
    }

