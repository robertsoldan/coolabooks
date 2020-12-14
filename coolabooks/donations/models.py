from django.db import models

# adding the model used for registering donations

class Donator(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    amount = models.CharField(max_length=10)
    address = models.CharField(max_length=400)
    postcode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)