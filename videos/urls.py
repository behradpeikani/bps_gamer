from django.urls import path 
from . import views


app_name = 'videos'
urlpatterns = [
	path('', views.VideoListView.as_view(), name='video-list'),
    path('<int:pk>/', views.VideoDetailView.as_view(), name='video-detail'),
]