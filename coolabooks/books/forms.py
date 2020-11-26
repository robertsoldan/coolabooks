from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'edition', 'author', 'location', 'genre', 'year', 'image']