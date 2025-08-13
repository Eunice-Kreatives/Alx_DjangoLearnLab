from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    API endpoint to create a new Book instance.

    - Requires authentication (IsAuthenticated).
    - Validates that no other book with the same title exists.
    - Logs the user who created the book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        """
        Handles custom creation logic before saving.
        - Prevents duplicate book titles.
        - Saves book to database.
        """
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise PermissionDenied("A book with this title already exists.")

        serializer.save()
        print(f"Book '{title}' was created by {self.request.user}.")
    
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  
    lookup_field = "pk"

    def perform_update(self, serializer):
        book = self.get_object()
        if book.author != self.request.user:
            raise PermissionDenied("You do not have permission to update this book.")
        serializer.save()
        print(f"Book '{book.title}' (ID: {book.id}) was updated by {self.request.user}.")


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] 
    lookup_field = "pk"

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You do not have permission to delete this book.")
        print(f"Book '{instance.title}' was deleted by {self.request.user}.")
        instance.delete()


