from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin




# view for the homepage

def index(request):

    # retrieving the stored object
    ind_books = Book.objects.all()

    context = {
        'ind_books':ind_books,
    }
    # rendering the template
    return render(request, 'books/index.html', context)

# view for the user dashboard

def mybooks(request):
    # retrieving the stored object
    ind_books = Book.objects.all()
    context = {
        'ind_books': ind_books,
    }

    return render(request, 'books/mybooks.html', context)

# view for the reserved section

def reserved(request):
    # retrieving the stored object
    ind_books = Book.objects.all()
    context = {
        'ind_books': ind_books,
    }

    return render(request, 'books/reserved.html', context)

# view for the disclaimer

def disclaimer(request):
    return render(request, 'books/disclaimer.html')

# view for the privacy page

def privacy(request):
    return render(request, 'books/privacy.html')

# class-based view for adding a book

class AddBook(SuccessMessageMixin, CreateView):
    model = Book
    fields = ['title', 'edition', 'author', 'location', 'genre', 'year', 'image']
    template_name = 'books/book-form.html'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)
    
    success_message = "%(title)s was created successfully"

# delete a book

def delete_book(request, id):
    ind_books = Book.objects.get(id=id)

    if request.method == 'POST':
        ind_books.delete()
        messages.success(request,f'{ ind_books.title } was successfully deleted.')
        return redirect('books:my-books')

    return render(request, 'books/delete-book.html', {'ind_books':ind_books})

# edit book information

def edit_book(request, id):
    ind_books = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance = ind_books)

    if form.is_valid():
        form.save()
        messages.success(request, f'{ ind_books.title } was successfully updated.')
        return redirect('books:my-books')
    
    return render(request, 'books/edit-book.html', {'form':form, 'ind_books': ind_books})

def search(request):

    # Filtering results in the order of which they are needed

    query = request.GET.get('search')
    result_title = Book.objects.filter(title__unaccent__icontains=query)
    result_author = Book.objects.filter(author__unaccent__icontains=query).difference(result_title)
    result_genre = Book.objects.filter(genre__unaccent__icontains=query).difference(result_title.union(result_author))
    result_location = Book.objects.filter(location__unaccent__icontains=query).difference(result_title.union(result_author, result_genre))

    final_result = result_title | result_author | result_genre | result_location

    context = {
        'result_title': result_title,
        'result_author': result_author,
        'result_genre': result_genre,
        'result_location': result_location,
    }
    # rendering the template
    return render(request, 'books/search.html', context)