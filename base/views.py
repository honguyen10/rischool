from django.shortcuts import render
import feedparser

# Create your views here.

def index(request):
    return render(request, 'base/index.html')

def about(request):
    return render(request, 'base/about.html')

def courses(request):
    return render(request, 'base/courses.html')

def blog(request):
    news_feed = feedparser.parse("https://bloghocpiano.com/feed/")
    feeds = news_feed.entries
    return render(request, 'base/blog.html',
                            {'feeds': feeds},
                             )

def contact(request):
    return render(request, 'base/contact.html')
