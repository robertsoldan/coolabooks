from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

# view to register the suers

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'{username}, time to log in for the first time!')
            return redirect('login')

    else:
        form = RegisterForm()
        
    return render(request, 'users/register.html', {'form':form})