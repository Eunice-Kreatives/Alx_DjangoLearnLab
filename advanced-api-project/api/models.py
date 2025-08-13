from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    """
    Represents an author who can have multiple books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book written by an author.
    - title: title of the book
    - publication_year: year the book was published
    - author: link to the author who wrote the book
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)      

    def __str__(self):
        return f"{self.title} ({self.publication_year})"