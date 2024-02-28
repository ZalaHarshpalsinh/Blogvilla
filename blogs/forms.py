from django import forms
from .models import User,Blog
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'image', 'content']
        help_texts = {
            'title' : 'Enter the blog title',
            'image' : 'Select a image for blog',
            'content' : 'Write your blog here',
        }
        error_messages = {
            "title": {
                "valid": "Please enter a valid title",
            }
        }

