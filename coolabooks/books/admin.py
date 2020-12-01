from django.contrib import admin
from .models import Book


# registering Book model in the admin panel
admin.site.register(Book)
admin.site.site_header = "Coola Books Admin Panel"
admin.site.site_title = "Coola Books"