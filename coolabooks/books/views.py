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

def mybooks(request):
    # retrieving the stored object
    ind_books = Book.objects.all()
    context = {
        'ind_books': ind_books,
    }

    return render(request, 'books/mybooks.html', context)

def reserved(request):
    # retrieving the stored object
    ind_books = Book.objects.all()
    context = {
        'ind_books': ind_books,
    }

    return render(request, 'books/reserved.html', context)

def disclaimer(request):
    return render(request, 'books/disclaimer.html')

def privacy(request):
    return render(request, 'books/privacy.html')