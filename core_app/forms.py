from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment', 'reply_to')
        widgets = {
            'reply_to': forms.HiddenInput(),
        }