from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Profile, User, Post
from .forms import Post_Form, Guess_Form



def email(request):
    return render(request, 'email.html')

def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')

def abyss(request):
    return render(request, 'abyss.html')
def fin(request):
    return render(request, 'fin.html')

def logout(request):
    auth.logout(request)
    return redirect('email')


def textscroll(request):
    return render(request, 'clues/textscroll.html')

def barcode(request):
    return render(request, 'clues/barcode.html')

def barcode1(request):
    return render(request, 'clues/barcode1.html')

def login(request):
    if request.method == 'POST':
        username_form = request.POST['username']
        password_form = request.POST['password']
    # authenticate user
        user = auth.authenticate(username=username_form, password=password_form)
        if user is not None:
            # login
            auth.login(request, user)
            #redirect
            profile = Profile.objects.get(user=user)
            return redirect('home')
        else:
            context = {'error':'Invalid Credentials'}
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return redirect('email')

# handles signup modal functionality POST request
def signup(request):
    if request.method == "POST":
        # build out data from form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username_form = request.POST['username']
        email_form = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # validate that passwords match
        if password1 == password2:
        # check if username exists in db
            if User.objects.filter(username=username_form).exists():
                context = {'error': 'Username is already taken.'}
                return render(request, 'home.html', context)
            else:
                if User.objects.filter(email=email_form).exists():
                    context = {'error':'That email already exists.'}
                    return render(request, 'home.html', context)
                else: 
                    # if everything is ok create account
                    user = User.objects.create_user(
                    username=username_form, 
                    email=email_form, 
                    password=password1, 
                    first_name=first_name, 
                    last_name=last_name)
                    user.save()
                    auth.login(request, user)
                    return redirect('home')
        else:
            context = {'error':'Passwords do not match'}
            return render(request, 'home.html', context)
    else:
        # if not post send form 
        return render(request, 'home.html')

# Route to handle creation of profile posts
def post_create(request, profile_id):
    success_message = ''
    if request.method == 'POST': 
        Post.objects.create(
            title = request.POST['title'],
            body = request.POST['body'],
            user = User.objects.get(id=request.user.id),
        )
        return redirect('profile', profile_id=profile_id)
    posts = Post.objects.filter(id=request.user.id)
    success_message = 'Post successful!'
    context = {'posts': posts, 'message': success_message}
    return render(request,'profile', context)



def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    else:
        print("Error")
    return redirect('profile/show.html', profile_id=profile.id)

def post_delete(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('home')

#def post_delete(request, post_id):
#    nextvalue = request.GET.get('next')
#    Post.objects.get(id=post_id).delete()
#    return redirect(nextvalue) 

def profile(request, profile_id):
    #found_profile = Profile.objects.get(id=user_id)
    profile = Profile.objects.get(id=profile_id)
    context = {'profile': profile}
    return render(request, 'profile/show.html', context)


def user_edit(request, profile_id):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
    else:
        print("TEST")
    return redirect('profile', profile_id=profile_id)

def guess_handle(request):
    form = Guess_Form()
    if request.method=='POST':
        form = Guess_Form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            guess = cd.get('guess')
            guess = guess.lower()
            if guess == "dhyhukwlhjl":
                return redirect('success')
            elif guess == "villanelle":
                return redirect('abyss')
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

