from django import forms
from . import models

class StudentFrom(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'