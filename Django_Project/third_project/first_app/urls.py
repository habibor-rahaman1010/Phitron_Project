from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name = 'myAbout'),
    path('blogs/', views.Blog, name = 'myBlogs'),
    path('service/', views.service, name = 'myService' ),
    path('submit/form', views.submit_form, name = 'submit'),
    path('django/form', views.DjangoForm, name = 'DjangoForm')
]