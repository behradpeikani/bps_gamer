from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from .models import Article, Category, Tag
from .forms import NewCommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.published()
    context_object_name = 'articles'
    paginate_by = 10


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    queryset = Article.objects.published()
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.published().exclude(pk=self.object.pk)[:3]

        article = self.get_object()

        allcomments = article.comments.filter(status=True)
        page = self.request.GET.get('page', 1)

        paginator = Paginator(allcomments, 10)
        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)

        user_comment = None

        context['comments'] = comments
        context['comment_form'] = NewCommentForm()
        context['allcomments'] = allcomments

        return context

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        comment_form = NewCommentForm(self.request.POST or None) 
        if self.request.method == 'POST':
              # comment_form = NewCommentForm(self.request.POST)
            if comment_form.is_valid():
                user_comment = comment_form.save(commit=False)
                user_comment.article = article
                user_comment.save()
                return redirect('blog:article-detail', slug=article.slug)
            else:
                comment_form = NewCommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        context['allcomments'] = allcomments

        return context


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




    
