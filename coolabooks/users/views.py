from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.apps import apps

# view to register the users


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # checks if the info submitted is valid (password, existing username...)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # once the user is registered and the form saved, we display a success message
            messages.success(request,f'{username}, your account has been successfully created. You can now safely log in.')
            # user is redirected to the login page so they can log in for the first time
            return redirect('login')

    else:
        form = RegisterForm()
        
    return render(request, 'users/register.html', {'form':form})



def profile(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        user.first_name = request.POST.get("fname", "")
        user.last_name = request.POST.get("lname", "")
        user.email = request.POST.get("email", "")
        user.save()
        return redirect('books:index')

    return render(request, 'users/profile.html')

def delete_user(request):
    user = User.objects.get(pk=request.user.id)

    if request.method == 'POST':

        book_model = apps.get_model('books', 'Book')
        reserved_books = book_model.objects.filter(reserved_by=user)

        for book in reserved_books:
            book.reserved_by = User.objects.get(username='admin')
            book.reserved = False
            book.save()

        posted_books = book_model.objects.filter(added_by=user)

        for book in posted_books:
            book.delete()

        user.is_active = False
        user.save()
        messages.success(request, 'User was deleted successfully, hope to see you again soon!')
        return redirect('books:index')

    return render(request, 'users/delete-user.html')