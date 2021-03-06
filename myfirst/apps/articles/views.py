from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article
from django.urls import reverse

def index(request):
    leatest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'leatest_articles_list': leatest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Статья не найдена!")
    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list':latest_comments_list})
