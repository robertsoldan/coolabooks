from . import views
from django.urls import path

# namespacing to avoid url confusion
app_name = 'books'

urlpatterns = [
    path('', views.index,name='index'),
]
