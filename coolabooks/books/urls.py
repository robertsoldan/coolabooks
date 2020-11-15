from . import views
from django.urls import path

# namespacing to avoid url confusion
app_name = 'books'

# we can add further paths here once we have set up the books model
urlpatterns = [
    path('', views.index,name='index'),
]
