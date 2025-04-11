from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . import views

# Views defined here for simplicity
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

def contact(request):
    return render(request, 'contact.html')

def kindergarten(request):
    return render(request, 'kindergarten.html')

def grades123(request):
    return render(request, 'grades123.html')

def grades45(request):
    return render(request, 'grades45.html')

def welcome_view(request):
    return render(request, 'welcome.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('welcome')  # Redirects to /welcome/
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'signin.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('help/', help, name='help'),
    path('contact/', contact, name='contact'),
    path('signin/', signin, name='signin'),
    path('kindergarten/', kindergarten, name='kindergarten'),
    path('grades123/', grades123, name='grades123'),
    path('grades45/', grades45, name='grades45'),
    path('welcome/', welcome_view, name='welcome'),
    path('abc-songs/', views.abc_songs, name='abc_songs'),
    path('math-songs/', views.math_songs, name='math_songs'),
    path('alphabet/', views.alphabet, name='alphabet'),
    path('colors/', views.colors, name='colors'),
    path('numbers/', views.numbers, name='numbers'),
    path('shapes/', views.shapes, name='shapes'),
]


# Serving static and media files (only in development)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
