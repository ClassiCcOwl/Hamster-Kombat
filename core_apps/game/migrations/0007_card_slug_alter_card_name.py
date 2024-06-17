# Generated by Django 5.0.6 on 2024-06-17 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_card_game_card_name_a356ae_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
