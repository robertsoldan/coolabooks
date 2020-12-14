
from . import views
from django.urls import path

# namespacing to avoid url confusion
app_name = 'books'

# we can add further paths here once we have set up the books model
urlpatterns = [
    path('', views.index, name='index'),
    path('my-books/', views.mybooks, name='my-books'),
    path('my-books/reserved/', views.reserved, name='reserved'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('privacy/', views.privacy, name='privacy'),
    path('about/', views.about, name='about'),
    path('add-book/', views.AddBook.as_view(), name='add_book'),
    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),
    path('edit-book/<int:id>/', views.edit_book, name='edit_book'),
    path('search/', views.search, name='search'),
    path('book/<int:id>', views.view_details, name='view_details'),
    path('<pk>/reserve/',views.ReserveBook.as_view(),name='reserve_book'),
    path('<pk>/cancel/',views.CancelBook.as_view(),name='cancel_book'),
]