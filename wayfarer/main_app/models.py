from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime

class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.CharField(max_length = 560)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField("Posted On", default= datetime.datetime.now)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    posts = models.CharField(max_length = 10)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

