from django.contrib import admin
from .models import Donator

# adding the Donator model to admin view
#admin.site.register(Donator)

class AdminDonator(admin.ModelAdmin):
    model = Donator
    list_display = ("name", "email", "amount")

admin.site.register(Donator, AdminDonator)