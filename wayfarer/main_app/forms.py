from django.forms import ModelForm
from .models import Puzzle

class Post_Form(ModelForm):
    class Meta:
      model = Puzzle
      labels = {'keyphrase': "Keyphrase"}
      fields = ['keyphrase']