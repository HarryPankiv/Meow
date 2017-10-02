from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
import urllib2
from .models import Article
#from .forms import RoomForm
from django.shortcuts import redirect
from django.http import HttpResponse

import json



# Create your views here.
def populate_db():
    # get articles
    url = 'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=bd83f8731650444684b1c3f7797f582a'
    response = urllib2.urlopen(url)
    articles = json.load(response)['articles']

    for each_article in articles:
        article = Article(author=each_article['author'],
                          title= each_article['title'],
                          description=each_article['description'],
                          url=each_article['url'],
                          url_to_image=each_article['urlToImage'],
                          publish_date=each_article['publishedAt'])
        try:
            article.save()
        except:
            print "fuck"
            return HttpResponse(status=403)
    return HttpResponse(status=200)





def start_page(request):
    populate_db()
    context = {
        'rooms': "dota",
    }
    return render(request, 'news_explorer/default.html', context)

