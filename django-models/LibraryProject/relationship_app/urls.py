# relationship_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
from django.contrib import admin