from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    avatar_img = models.ImageField()
    bio = models.TextField()
    birth_date = models.DateField(blank=True, null=True)
    follows = models.ManyToManyField('self')


class Card(models.Model):
    PRIVACY_CHOICES = [(False, 'Private'), (True, 'Public')]

    sender = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='cards_to_sender')
    receiver = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='cards_to_receiver')
    text = models.CharField(max_length=300)
    image_urls = models.URLField(max_length=500)
    date_created = models.DateTimeField()
    privacy = models.BooleanField(default=True, choices=PRIVACY_CHOICES)
    headline = models.CharField(max_length=300)
    front_text = models.TextField()
    back_text = models.TextField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()


# class Draft(models.Model): ???
