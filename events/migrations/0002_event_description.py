# Generated by Django 2.1 on 2018-08-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default="It's an event, get up and going!", max_length=700),
        ),
    ]
