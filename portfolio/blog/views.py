from django.shortcuts import render, get_object_or_404
from .models import Article


def blog(request):
    
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, 'blog/index.html', context)

def show(request, id):
    article = get_object_or_404(Article, pk=id)

    from django.conf import settings
    # settings = settings.MEDIA_URL

    context = {
        "article" : article,
        # "settings" : settings
    }
    return render(request, 'blog/article.html', context)