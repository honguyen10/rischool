from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index.html'),
    path('about', views.about, name='about.html'),
    path('courses', views.courses, name='courses.html'),
    path('news', views.news, name='news.html'),
    path('contact', views.contact, name='contact.html'),

]
