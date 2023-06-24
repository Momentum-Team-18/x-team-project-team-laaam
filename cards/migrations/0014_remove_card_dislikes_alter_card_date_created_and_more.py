# Generated by Django 4.2.2 on 2023-06-24 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0013_card_border_decor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='dislikes',
        ),
        migrations.AlterField(
            model_name='card',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='sent_by_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cards_sent', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='sent_to_user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='cards_received', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
