# Generated by Django 3.0.6 on 2020-05-13 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobinator', '0003_auto_20200511_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinator',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]