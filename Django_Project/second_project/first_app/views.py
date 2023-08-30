from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return HttpResponse(''' 
                            <h1>This is my contact page over there!</h1>
                            <a href='/first_app/about/'> about </a>
                            <a href='/second_app/product/'> product</a>
                            <a href='/second_app/service/'> service </a>
                        ''')

def about(request):
    return HttpResponse(''' 
                            <h1>This is my about page over there!</h1>
                            <a href='/first_app/contact/'> contact </a>
                            <a href='/second_app/product/'> product</a>
                            <a href='/second_app/service/'> service </a>
                        ''')
