from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book

# Create your views here.

def index(request):

    # retrieving the stored object
    ind_books = Book.objects.all()

    # empty context for now
    context = {
        'ind_books':ind_books,
    }
    # rendering the template
    return render(request, 'books/index.html', context)