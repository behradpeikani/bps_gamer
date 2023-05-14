from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import get_object_or_404
from .models import Article, Category, Tag
from .forms import CommentForm

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class AddCommentView(FormView):
    form_class = CommentForm
    template_name = 'blog/article_detail.html'

    def form_valid(self, form):
        article = get_object_or_404(Article, slug=self.kwargs['slug'])
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article-detail', kwargs={'slug': self.kwargs['slug']})
