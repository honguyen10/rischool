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
    # feeds_information = news_feed.feed
    # latest = news_feed.entries[:3]
    return render(request, 'base/blog.html',
                {'feeds': feeds},
                # {'feeds_information': feeds_information},
                # {'latest': latest},
                )

def contact(request):
    return render(request, 'base/contact.html')
