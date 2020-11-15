from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):

    # empty context for now
    context = {

    }
    # rendering the template
    return render(request, 'books/index.html', context)