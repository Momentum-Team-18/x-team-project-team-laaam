# Generated by Django 4.2.2 on 2023-06-24 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0011_card_border_decor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='border_decor',
        ),
    ]