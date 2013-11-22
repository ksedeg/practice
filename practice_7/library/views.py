#!/usr/bin/python
# -*- coding: utf-8 -*-

#from django.db import connection
#from django.template.loader import get_template
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from library.models import *
from django.views.generic import *

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class BookListView(ListView):
    template_name = "cbv-books.html"
    model = Book


class BookCardView(DetailView):
    template_name = "cbv-book_data.html"
    queryset = Book.objects.all()


class AuthorsListView(ListView):
    template_name = "cbv-authors.html"
    model = Author


class AuthorCardView(DetailView):
    template_name = "cbv-author_card.html"
    queryset = Author.objects.all()


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

"""
def index(request):
    books = {}
    for b in Book.objects.all():
        bookAuthors = []
        for a in b.authors.all():
            bookAuthors.append(a.__unicode__())
        curson = connection.cursor()
        curson.execute("SELECT id FROM library_book WHERE title = %s", [b.title])
        id = curson.fetchall()[0]
        books[id]={'id': id[0], 'abs_url': b.get_absolute_url(), "title": b.title, "authors": bookAuthors, "publisher": b.publisher.__unicode__()}
    return render_to_response('books.html', {'books': books})


def bookCard(request, id):
    book = Book.objects.raw("SELECT * FROM library_book WHERE id = %s", [id])[0]
    IDs = connection.cursor()
    IDs = IDs.execute("SELECT A.id FROM library_author AS A JOIN library_book_authors AS B ON A.id=B.id WHERE B.book_id = %s", [id])
    authors={}
    for i, a in zip(IDs.fetchall(), book.authors.all()):
        authors[str(i[0])]=a.__unicode__()
    book_data = {'id': id, 'title': book.__unicode__(), 'authors': authors, 'publisher': book.publisher.__unicode__(), 'publication_date': str(book.publication_date)}
    return render_to_response('book_data.html', {'book_data': book_data})


def authors(request):
    authors = {}
    for a in Author.objects.all():
        authorId = connection.cursor()
        authorId = authorId.execute("SELECT id FROM library_author WHERE first_name=%s AND last_name=%s", [a.first_name, a.last_name])
        ID = authorId.fetchall()[0][0]
        authors[str(ID)]=a.__unicode__()
    return render_to_response('authors.html', {'authors': authors})


def authorsCard(request, id):
    author = Author.objects.raw("SELECT * FROM library_author WHERE id = %s", [id])[0]
    return HttpResponse(render_to_response('author_card.html', {'author': author}))"""
