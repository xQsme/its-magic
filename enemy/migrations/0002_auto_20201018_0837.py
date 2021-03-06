# Generated by Django 3.1.2 on 2020-10-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enemy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemy',
            name='currentHP',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='enemy',
            name='currentMana',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='enemy',
            name='damage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='enemy',
            name='mana',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
