from django import forms
from .models import Comment, ContactUs


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
        {"placeholder": "Enter Your Name",
        "class": "form-control"
        }))

    email = forms.EmailField(widget=forms.EmailInput(attrs=
        {"placeholder": "Enter Your Email",
        "class": "form-control"
        }))

    message = forms.CharField(widget=forms.Textarea(attrs=
        {"placeholder": "Type Your Comment",
        "class": "form-control",
        "rows": 10, "cols": 40,
        "style": "resize: none;"
        }))


    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message')