from .models import Tag, Article

def tags_processor(request):
    tags = Tag.objects.all()
    return {'tags': tags}

def articles_processor(request):
    articles = Article.objects.published()
    return {'articles': articles}