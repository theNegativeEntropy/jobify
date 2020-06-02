# Generated by Django 3.0.6 on 2020-06-02 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraper', '0014_website_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='website',
            field=models.CharField(default='Indeed', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='website',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
