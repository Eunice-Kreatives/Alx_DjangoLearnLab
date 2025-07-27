from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    search_term = request.GET.get('q', '')  # Get 'q' parameter from URL
    if search_term:
        books = Book.objects.filter(title__icontains=search_term)
    else:
        books = Book.objects.all()
    
    return render(request, 'bookshelf/book_list.html', {
        'book_list': books,
        'search_term': search_term
    })

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # TODO: Add form handling logic here
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # TODO: Add form handling logic here
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')


def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # process data
            pass
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/example_form.html', {'form': form})
