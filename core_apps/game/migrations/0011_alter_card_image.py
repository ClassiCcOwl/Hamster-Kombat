# Generated by Django 5.0.6 on 2024-06-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_alter_card_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(default='default.png', upload_to='card_images/'),
        ),
    ]
