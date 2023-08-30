from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('store/book/', views.store_books, name='store_book'),
    path('show/books/', views.show_books, name='show_books'),
    path('edit/books/<int:id>', views.edit_book, name='edit_book'),
    path('delete/books/<int:id>', views.delete_book, name='delete_book'),
]
