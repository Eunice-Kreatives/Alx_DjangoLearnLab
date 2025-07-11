# Retrieve all books
from bookshelf.models import Book
Book.objects.all()

# Output:
# <QuerySet [<Book: 1984>]>
