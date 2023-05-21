from django.shortcuts import render
from .models import Book
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    books_title = Book.objects.all()
    return render(request, 'book_outlet/book_list.html', {'books': books})


def index(request):
    return render(request, "book_outlet/index.html")