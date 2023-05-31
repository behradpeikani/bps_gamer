from django.urls import path
from . import views


app_name = 'core_app'
urlpatterns = [
	path('about-us/', views.AboutUsPage.as_view(), name='about-us'),
	path('contact-us/', views.ContactUsView.as_view(), name='contact-us'),
]