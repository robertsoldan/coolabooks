from django.shortcuts import render, redirect
from .models import Donator 
from django.contrib import messages

# pulling in the information submitted by the user and rendering a message confirming the amount donated

def donate(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        amount = request.POST.get("amount", "")
        address = request.POST.get("address", "")
        postcode = request.POST.get("postcode", "")
        city = request.POST.get("city", "")
        country = request.POST.get("country", "")

        donator = Donator(name=name, email=email, amount=amount, address=address, postcode=postcode, city=city, country=country)
        donator.save()
        messages.success(request,f'{name}, thank you for supporting our project with the donation of {amount} €.')
        return redirect('books:index')
        
    return render(request, 'donations/donation.html') 
