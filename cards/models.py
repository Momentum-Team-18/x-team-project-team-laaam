from typing import Any
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    avatar_img = models.ImageField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username


class Follow(models.Model):
    this_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='follows_user', blank=True, null=True)
    user_this_user_is_following = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='follows_these_users', blank=True, null=True)
    # user_following_this_user = models.ForeignKey(
    #     to='self', on_delete=models.CASCADE, related_name='follows_this_user')

    def __str__(self):
        return str(self.this_user)


class Card(models.Model):
    PRIVACY_CHOICES = [(False, 'Private'), (True, 'Public')]

    SCRIPT = 'Script'
    SERIF = 'Serif'
    SANS_SERIF = 'Sans Serif'
    FONT_CHOICES = [(SCRIPT, 'Script'), (SERIF, 'Serif'),
                    (SANS_SERIF, 'Sans Serif')]
    BLUE = 'Blue'
    YELLOW = 'Yellow'
    RED = 'Red'
    PURPLE = 'Purple'
    ORANGE = 'Orange'
    COLOR_CHOICES = [(BLUE, 'Blue'), (YELLOW, 'Yellow'),
                     (RED, 'Red'), (PURPLE, 'Purple'), (ORANGE, 'Orange')]

    DOTTED = 'Dotted'
    SOLID = 'Solid'
    NO_BORDER = 'No Border'
    BORDER_CHOICES = [(DOTTED, 'Dotted'), (SOLID, 'Solid'),
                      (NO_BORDER, 'No Border')]

    sent_by_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='cards_sent')
    sent_to_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='cards_received')

    image_urls = models.URLField(max_length=500, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    privacy = models.BooleanField(default=True, choices=PRIVACY_CHOICES)
    headline = models.CharField(max_length=300)
    front_text = models.TextField(blank=True, null=True)
    back_text = models.TextField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    background_color = models.CharField(
        blank=True, null=True, choices=COLOR_CHOICES)
    border_color = models.CharField(
        blank=True, null=True, choices=COLOR_CHOICES)
    border_decor = models.CharField(
        blank=True, null=True, choices=BORDER_CHOICES)
    font_color = models.CharField(blank=True, null=True, choices=COLOR_CHOICES)
    header_font = models.TextField(blank=True, null=True)
    front_text_font = models.TextField(
        blank=True, null=True, choices=FONT_CHOICES)
    back_text_font = models.TextField(
        blank=True, null=True, choices=FONT_CHOICES)

    def __str__(self):
        return self.headline


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
