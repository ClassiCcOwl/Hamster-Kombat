# Generated by Django 5.0.6 on 2024-06-23 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0018_alter_card_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['category__created_at', 'created_at']},
        ),
    ]
