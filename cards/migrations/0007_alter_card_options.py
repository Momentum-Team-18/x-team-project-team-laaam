# Generated by Django 4.2.2 on 2023-06-28 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_remove_card_back_text_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['-date_created']},
        ),
    ]
