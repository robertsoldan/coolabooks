from django.db import models
import datetime

class Contact(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=10000)
    date = models.CharField(max_length=100, default=datetime.datetime.now())
