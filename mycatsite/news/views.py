# Create your views here.
from django.shortcuts import render
from .models import News_post

def news_list(request):
    news = News_post.objects.all().order_by('-pub_date')
    return render(request, 'news/news.html', {'news': news})