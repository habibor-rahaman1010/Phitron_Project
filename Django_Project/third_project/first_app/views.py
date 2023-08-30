from django.shortcuts import render
from . forms import contactForm

# Create your views here.

def about(request):
    return render(request, 'first_app/about.html')

def Blog(request):
    return render(request, 'first_app/blogs.html')

def service(request):
    return render(request, 'first_app/service.html')

def submit_form(request):
    if(request.method == "POST"):
        name = request.POST.get('userName')
        email = request.POST.get('userEmail')
        select = request.POST.get('select')
        return render(request, 'first_app/form.html', context={'name': name, 'email': email, 'select': select})
    else:
        return render(request, 'first_app/form.html')


def DjangoForm(request):
    if(request.method == "POST"):
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            form = contactForm()
            return render(request, 'first_app/django_form.html', context={'form': form, 'name': name, 'email': email})
        else:
            return render(request, 'first_app/django_form.html', context={'form': form})
    else:
        form = contactForm()
        return render(request, 'first_app/django_form.html', context={'form': form})