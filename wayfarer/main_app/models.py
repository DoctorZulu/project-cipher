from django.db import models
from django.contrib.auth.models import User
import datetime

class Puzzle(models.Model):
    name = models.CharField(max_length = 50)
    date = models.DateTimeField("Solved On", default = datetime.datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyphrase = models.ForeignKey(max_Length = 50)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['date']