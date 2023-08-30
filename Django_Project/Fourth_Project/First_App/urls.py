from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete_student/<int:roll>', views.delete_student, name='delete_student')
]
