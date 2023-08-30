from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def service(request):
    return HttpResponse(''' 
                            <h1>This is my service page over there!</h1>
                            <a href='/second_app/product/'> product</a>
                            <a href='/first_app/about/'> about </a>
                            <a href='/first_app/contact/'> contact </a>
                        ''')

def product(request):
    return HttpResponse(''' 
                            <h1>This is my product page over there!</h1>
                            <a href='/second_app/service/'> service </a>
                            <a href='/first_app/about/'> about </a>
                            <a href='/first_app/contact/'> contact </a>
                        ''')
