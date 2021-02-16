from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


def first(request):
    return HttpResponse('Hello world')


class Second(View):
    books = Book.objects.all()
    output = ''
    output += f'We have {len(books)} in our Database<br>'

    for book in books:
        output += f'We have {book.title} with ID {book.id} in our Database<br>'
    books = Book.objects.filter(is_published=True)

    for book in books:
        output += f'We have {len(books)} published books in our Database<br>'

    book=Book.objects.get(id=1)
    output += f'Our favourite book is {book.title} <br>'

    def get(self, request):
        return HttpResponse(self.output)
