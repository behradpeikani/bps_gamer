from .models import Category, Article

def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}

def articles_processor(request):
    articles = Article.objects.published()
    return {'articles': articles}