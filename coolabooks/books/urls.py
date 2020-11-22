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
]