# Generated by Django 5.0.6 on 2024-06-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_alter_card_image'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='level',
            index=models.Index(fields=['level'], name='game_level_level_0eecce_idx'),
        ),
    ]
