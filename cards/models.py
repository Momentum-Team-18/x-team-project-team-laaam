from typing import Any
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    avatar_img = models.ImageField()
    bio = models.TextField()
    birth_date = models.DateField(blank=True, null=True)
    follows = models.ManyToManyField('self')

    def __str__(self):
        return self.username


class Card(models.Model):
    PRIVACY_CHOICES = [(False, 'Private'), (True, 'Public')]

    sender = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='cards_to_sender')
    receiver = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='cards_to_receiver')
    image_urls = models.URLField(max_length=500)
    date_created = models.DateTimeField()
    privacy = models.BooleanField(default=True, choices=PRIVACY_CHOICES)
    headline = models.CharField(max_length=300)
    front_text = models.TextField()
    back_text = models.TextField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    background_color = models.CharField(blank=True, null=True)
    border_color = models.CharField(blank=True, null=True)
    font_color = models.CharField(blank=True, null=True)
    header_font = models.TextField()
    front_text_font = models.TextField()
    back_text_font = models.TextField()

    def __str__(self):
        return self.header

class Comment(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='comments_by_user'
    )
    card = models.ForeignKey(
        to=Card, on_delete=models.CASCADE, related_name='comments_on_card'
    )
    body = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body