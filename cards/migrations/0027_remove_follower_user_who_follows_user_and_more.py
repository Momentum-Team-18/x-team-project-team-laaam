# Generated by Django 4.2.2 on 2023-06-25 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0026_remove_user_follower_bool_user_follower_bool'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='user_who_follows_user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follower_user',
        ),
    ]
