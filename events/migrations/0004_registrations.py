# Generated by Django 2.1 on 2018-08-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=40)),
            ],
        ),
    ]
