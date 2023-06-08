from django.views.generic import ListView, DetailView
from .models import Video
from django.shortcuts import get_object_or_404


class VideoListView(ListView):
	model = Video
	template_name = 'videos/video_list.html'
	context_object_name = 'videos'
	paginate_by = 10


class VideoDetailView(DetailView):
	model = Video
	template_name = 'videos/video_detail.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		video_id = self.kwargs.get('pk')
		context["video"] = get_object_or_404(Video, pk=video_id)
		return context