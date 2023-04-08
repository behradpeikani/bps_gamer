from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutUs


class AboutUsPage(TemplateView):
	template_name = 'core_app/about_us_page.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['obj'] = AboutUs.objects.all()

		return context 
