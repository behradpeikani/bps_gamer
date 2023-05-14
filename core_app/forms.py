from django import forms
from .models import Comment, ContactUs


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment', 'reply_to')
        widgets = {
            'reply_to': forms.HiddenInput(),
        }


class ContactForm(forms.Form):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message')