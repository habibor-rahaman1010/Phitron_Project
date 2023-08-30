from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name = 'djangomart'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
