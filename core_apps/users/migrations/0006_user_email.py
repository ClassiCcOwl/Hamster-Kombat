# Generated by Django 5.0.6 on 2024-07-11 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]