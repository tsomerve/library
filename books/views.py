from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def check_out(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.checked_out = True
        book.save()
    return redirect('book_detail', pk=book.pk)

def check_in(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.checked_out = False
        book.save()
    return redirect('book_detail', pk=book.pk)
