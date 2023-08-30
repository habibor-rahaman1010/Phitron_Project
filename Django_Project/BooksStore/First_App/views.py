from django.shortcuts import render, redirect
from . import forms, models

# Create your views here.
def index(request):
    return render(request, './First_Template/index.html')

def store_books(request):
    if(request.method == 'POST'):
        book = forms.BookStoreForm(request.POST)
        if(book.is_valid()):
            book.save()
            book = forms.BookStoreForm()
            return redirect('show_books')
    else:
        book = forms.BookStoreForm()
    return render(request, './First_Template/store_book.html', context={'form': book})

def show_books(request):
    books = models.BookStroeModel.objects.all()
    return render(request, './First_Template/show_books.html', context={'books': books})

def edit_book(request, id):
    book = models.BookStroeModel.objects.get(pk = id)
    form  = forms.BookStoreForm(instance=book)
    if(request.method == 'POST'):
        book = forms.BookStoreForm(request.POST, instance=book)
        if(book.is_valid()):
            book.save()
            book = forms.BookStoreForm()
            return redirect('show_books')
    return render(request, './First_Template/edit_book.html', context={'form': form, 'book': book})

def delete_book(request, id):
    models.BookStroeModel.objects.get(pk = id).delete()
    return redirect('show_books')
