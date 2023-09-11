from django.db import models
from django.contrib.auth.models import User

# User Profile Model (for user preferences)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_genres = models.ManyToManyField('Genre', blank=True)
    favorite_authors = models.ManyToManyField('Author', blank=True)
    favorite_books = models.ManyToManyField('Book', blank=True)

    def __str__(self):
        return self.user.username

# Genre Model
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    synopsis = models.TextField()
    cover_image_url = models.URLField()

    def __str__(self):
        return self.title
    # Add other book-related fields like ratings, comments, etc.

# User Interaction Model
class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status_choices = (
        ('Read', 'Read'),
        ('Want to Read', 'Want to Read'),
        ('Currently Reading', 'Currently Reading'),
    )
    status = models.CharField(max_length=20, choices=status_choices)
    progress = models.PositiveIntegerField(default=0, help_text="Reading progress in percentage")

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.status})"
