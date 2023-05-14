from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .models import AboutUs, Comment
from .forms import CommentForm, ContactForm


class AboutUsPage(TemplateView):
	template_name = 'core_app/about_us_page.html'
	form_class = CommentForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['obj'] = AboutUs.objects.first()
		# context['comments'] = Comment.objects.filter(parent_isnull=True)
		context['comments'] = Comment.objects.all()
		context['form'] = self.form_class
		return context

	def post(self, request, *args, **kwargs):
		form = self.form_class
		if form.is_valid():
			comment = form.save(commit=False)
			if request.POST.get('reply_to'):
				comment.parent_id = request.POST.get('reply_to')
			comment.save()
			return redirect('about-us/')
		else:
			return self.form_invalid(form)


class ContactUsView(FormView):
    template_name = 'core_app/contact-us-page.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-us')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)