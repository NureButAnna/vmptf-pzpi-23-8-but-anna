from wsgiref.util import request_uri

from django.shortcuts import render, get_object_or_404
from .models import Article
from rest_framework import generics
from .serializers import ArticleSerializer

def article_list(request):
    articles = Article.objects.order_by('date')

    author = request.GET.get('author')
    if author:
        articles = articles.filter(author=author)

    authors = Article.objects.values_list('author', flat=True).distinct()

    return render(request, 'news/article_list.html', {
        'articles': articles,
        'authors': authors
    })


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'news/article.html', {'article': article})

class NewsAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer