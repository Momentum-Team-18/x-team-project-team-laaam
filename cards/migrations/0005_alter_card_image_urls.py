# Generated by Django 4.2.2 on 2023-06-22 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_remove_card_text_card_back_text_font_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image_urls',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]