from django.contrib import admin
from .models import Donator

# adding the Donator model to admin view
admin.site.register(Donator)