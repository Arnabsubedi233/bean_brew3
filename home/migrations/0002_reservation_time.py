# Generated by Django 5.0.1 on 2024-03-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]