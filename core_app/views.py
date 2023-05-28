from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .models import AboutUs, Comment, ContactUs
from .forms import CommentForm, ContactForm
from django.contrib import messages


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
	success_url = reverse_lazy('core_app:contact-us')

	def form_valid(self, form):
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			ContactUs.objects.create(name=name, email=email, message=message)
			messages.success(self.request, 'Your message has been sent successfully.', 'success')
			return super().form_valid(form)
		else:
			messages.error(self.request, 
				'Something went wrong! Please try again.', 'warning')
			return redirect('core_app:contact-us')