from django.shortcuts import render
from .models import Article


def blog(request):

    
    articles = Article.objects.all()

    context = {
        "articles": articles
    }

    return render(request, 'blog/index.html', context)