# Generated by Django 3.2.15 on 2022-09-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
