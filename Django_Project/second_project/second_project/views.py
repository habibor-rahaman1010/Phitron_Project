# This is my all about controllers in django
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello Programmer</h1>")
