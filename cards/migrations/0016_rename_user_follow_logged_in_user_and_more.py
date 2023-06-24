# Generated by Django 4.2.2 on 2023-06-24 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0015_user_follows'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='user',
            new_name='logged_in_user',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='user_follows',
            new_name='user_who_user_follows',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follows',
        ),
    ]
