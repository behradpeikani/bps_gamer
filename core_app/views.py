from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import AboutUs, ContactUs
from .forms import ContactForm
from django.contrib import messages
from blog.models import Article, Tag


class HomepageView(ListView):
    template_name = 'core_app/home_page.html'
    queryset = Article.objects.published()
    context_object_name = 'articles'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()[:10]
        return context


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
            messages.success(self.request,
             'Your message has been sent successfully.', 'success')
            return super().form_valid(form)
        else:
            messages.error(self.request, 
                'Something went wrong! Please try again.', 'warning')
            return redirect('core_app:contact-us')


class AboutUsPage(TemplateView):
    template_name = 'core_app/about_us_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = AboutUs.objects.first()
        return context
