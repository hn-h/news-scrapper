from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as BSoup
from newsApp.models import News

from rest_framework import viewsets
from .serializers import NewsSerializer


def scrape(request):
    News.objects.all().delete()
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    articles = soup.find_all('article')

    for article in articles:
        title = article.find('h4').get_text()
        link = article.find('a')['href']
        img = article.find('img')
        try:
            img=img['srcset'].split(" ")[-4]
        except:
            img = 'https://www.via-ks.com/wp-content/uploads/2017/01/news-images-3.jpg'
        new_headline = News()
        new_headline.title = title
        new_headline.image = img
        new_headline.url = link
        new_headline.save()

    return redirect('/api/news/'+str(News.objects.first().id))

class NewsAPIView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
