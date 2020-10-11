# Generated by Django 3.1.2 on 2020-10-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201011_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemy',
            name='life',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='spell',
            name='damage',
            field=models.PositiveIntegerField(default=0),
        ),
    ]