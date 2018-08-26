from django.db import models

class Event(models.Model):
    category = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.DateField('Event Date')
    description = models.CharField(max_length=700, default="It's an event, get up and going!")
    contact = models.CharField(max_length=13, default='+91')


class Registrations(models.Model):
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=40)



