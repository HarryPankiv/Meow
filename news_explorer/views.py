from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
import urllib2
from .models import Article
from django.db import IntegrityError
#from .forms import RoomForm
from django.shortcuts import redirect
from django.http import HttpResponse

import json


def create(url, tag):
    response = urllib2.urlopen(url)
    articles = json.load(response)['articles']

    for each_article in articles:
        article = Article(author=each_article['author'],
                          title=each_article['title'],
                          description=each_article['description'][:150],
                          url=each_article['url'],
                          url_to_image=each_article['urlToImage'],
                          publish_date=each_article['publishedAt'],
                          tag=tag)
        try:
            article.save()
        except IntegrityError:
            pass


# Create your views here.
def populate_db():
    # get articles
    url = 'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=bd83f8731650444684b1c3f7797f582a'
    response = urllib2.urlopen(url)
    articles = json.load(response)['articles']

    urls = {
        'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=bd83f8731650444684b1c3f7797f582a': 'bbc-news',
        'https://newsapi.org/v1/articles?source=bbc-sport&sortBy=top&apiKey=bd83f8731650444684b1c3f7797f582a': 'bbc-sports',
        #'https://newsapi.org/v1/articles?source=hacker-news&sortBy=top&apiKey=bd83f8731650444684b1c3f7797f582a': 'hacker-news',
        'https://newsapi.org/v1/articles?source=mtv-news&sortBy=top&apiKey=bd83f8731650444684b1c3f7797f582a': 'mtv-news'
    }

    for url in urls:
        create(url, urls[url])

    return HttpResponse(status=200)



def start_page(request):
    populate_db()
    articles = Article.get_all_articles()
    context = {
        'articles': articles,
        'page': 'home'
    }
    return render(request, 'news_explorer/default.html', context)

def music_page(request):
    articles = Article.objects.filter(tag='mtv-news')
    context = {
        'articles': articles,
        'page': 'music'
    }
    return render(request, 'news_explorer/default.html', context)

