from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import get_object_or_404
from .models import Article, Category, Tag


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'


class TagView(ListView):
    template_name = 'blog/tag_view.html'
    model = Tag
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        context["tag"] = get_object_or_404(Tag, random_id=tag_id)
        return context


class CategoryView(ListView):
    template_name = 'blog/category_view.html'
    model = Category
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context["category"] = get_object_or_404(Category, slug=slug)
        return context



    
