from django.contrib import admin
from .models import Book


# registering Book model in the admin panel
admin.site.register(Book)