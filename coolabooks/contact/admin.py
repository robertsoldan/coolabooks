from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact

# adding the Contact model to admin view
#admin.site.register(Contact)

class AdminContact(admin.ModelAdmin):
    model = Contact
    list_display = ('name', 'email', 'message', 'date')


admin.site.register(Contact, AdminContact)