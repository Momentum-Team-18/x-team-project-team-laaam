# Generated by Django 4.2.2 on 2023-06-27 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='user_following_this_user',
        ),
    ]
