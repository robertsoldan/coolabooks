from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

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