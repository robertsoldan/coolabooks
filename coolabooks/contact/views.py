from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        message = request.POST.get("message", "")

        contact_request = Contact(name=name, email=email, message=message)
        contact_request.save()
        messages.success(request, "Thank you for your message, we will be in touch as soon as possible!")
        return redirect('books:index')

    return render(request, 'contact/contact.html')