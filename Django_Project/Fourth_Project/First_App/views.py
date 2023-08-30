from django.shortcuts import render, redirect
from . import models
from . import forms

# Create your views here.

def index(request):
    student = models.Student.objects.all()
    student_form = forms.StudentFrom()
    if(request.method == "POST"):
        form = forms.StudentFrom(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
        else:
            form = forms.StudentFrom()
    return render(request, 'index.html', context={'students':student, 'student_form': student_form})


def delete_student(request, roll):
    student = models.Student.objects.get(pk = roll).delete()
    return redirect('home')
