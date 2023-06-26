# Generated by Django 4.2.2 on 2023-06-25 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0017_remove_follow_logged_in_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='user_as_follower',
            new_name='user_is_following',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='user_being_followed',
        ),
        migrations.AddField(
            model_name='follow',
            name='user_being_followed_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='follows_this_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
