# Generated by Django 3.1.2 on 2020-10-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enemy', '0002_auto_20201018_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemy',
            name='sound',
            field=models.FileField(default='', upload_to='uploads/'),
        ),
    ]
