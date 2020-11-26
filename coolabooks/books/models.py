from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Books model that includes the fields needed to add a book

class Book(models.Model):

    # returns the book as the title String
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    edition = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    loc_choice = (
        ('Dublin 1', 'Dublin 1'),
        ('Dublin 2', 'Dublin 2'),
        ('Dublin 3', 'Dublin 3'),
        ('Dublin 4', 'Dublin 4'),
        ('Dublin 5', 'Dublin 5'),
        ('Dublin 6', 'Dublin 6'),
        ('Dublin 7', 'Dublin 7'),
        ('Dublin 8', 'Dublin 8'),
        ('Dublin 9', 'Dublin 9'),
        ('Dublin 10', 'Dublin 10'),
        ('Dublin 11', 'Dublin 11'),
        ('Dublin 12', 'Dublin 12'),
        ('Dublin 13', 'Dublin 13'),
        ('Dublin 14', 'Dublin 14'),
        ('Dublin 15', 'Dublin 15'),
        ('Dublin 16', 'Dublin 16'),
        ('Dublin 17', 'Dublin 17'),
        ('Dublin 18', 'Dublin 18'),
        ('Dublin 19', 'Dublin 19'),
        ('Dublin 20', 'Dublin 20'),
        ('Dublin 21', 'Dublin 21'),
        ('Dublin 22', 'Dublin 22'),
        ('Dublin 23', 'Dublin 23'),
        ('Dublin 24', 'Dublin 24'),      
    )
    location = models.CharField(max_length=30, choices=loc_choice)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.CharField(max_length=300, default="https://images.pexels.com/photos/4199098/pexels-photo-4199098.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940")
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="added_book",
        default=1
    )
    reserved = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )

    # adding redirect after the book has been added
    def get_absolute_url(self):
        return reverse("books:my-books")