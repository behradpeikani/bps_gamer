from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
	path('', views.ArticleListView.as_view(), name='article-list'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('tag/<int:tag_id>/', views.TagView.as_view(), name='tag-view')
]

