CRUD Operations via Django Shell

## 1. Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

## 2. Retrieve

Book.objects.all()

## 3. Update

book.title = "Nineteen Eighty-Four"
book.save()
book

## 4. Delete

book.delete()
Book.objects.all()
