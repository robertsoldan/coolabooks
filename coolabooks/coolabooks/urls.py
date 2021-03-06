"""coolabooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from django.contrib.auth import views as authentication_views
from django.urls import include, path
from donations import views as donation_views
from contact import views as contact_views



urlpatterns = [
    # plugs the urls from the books directory to the main url patterns
    path('', include('books.urls')),
    # plugs in admin url
    path('admin/', admin.site.urls),
    # setting up URL pattern for register function
    path('register/', user_views.register, name='register'),
    # setting up URL patterns for login and logout
    path('login/', authentication_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('delete-user/', user_views.delete_user, name='delete-user'),
    # setting up URL pattern for the donation
    path('donate/', donation_views.donate, name="donate"),
    # setting up URL pattern for the contact page
    path('contact/', contact_views.contact, name="contact"),
]
