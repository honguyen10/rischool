from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'base/index.html')

def about(request):
    return render(request, 'base/about.html')

def courses(request):
    return render(request, 'base/courses.html')

def news(request):
    return render(request, 'base/news.html')

def contact(request):
    return render(request, 'base/contact.html')
