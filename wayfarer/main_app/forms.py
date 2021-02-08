from django.forms import ModelForm
from .models import Post
from django.contrib.auth.forms import forms

class Post_Form(ModelForm):
    class Meta:
      model = Post 
      labels = {'title': "Post Title"}
      fields = ['title','body']

