# in views.py
from django.shortcuts import render

def signin_view(request):
    return render(request, 'signin.html')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

def contact(request):
    return render(request, 'contact.html')

def signin(request):
    return render(request, 'signin.html')

def kindergarten(request):
    return render(request, 'kindergarten.html')

def grades123(request):
    return render(request, 'grades123.html')

def grades45(request):
    return render(request, 'grades45.html')

def index(request):
    return render(request, 'index.html')

def welcome_view(request):
    return render(request, 'welcome.html')

def abc_songs(request):
    return render(request, 'ABC Songs.html')

def math_songs(request):
    return render(request, 'math songs.html')

def alphabet(request):
    return render(request, 'alphabet.html')

def colors(request):
    color_list = [
        'red', 'green', 'blue', 'orange', 'purple',
        'yellow', 'pink', 'brown', 'teal',
        'black', 'gray', 'white'
    ]
    return render(request, 'color.html', {'colors': color_list})


def numbers(request):
    return render(request, 'numbers.html')

def shapes(request):
    return render(request, 'shapes.html')

