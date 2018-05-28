from django import forms
from .models import Blog
from martor.fields import MartorFormField

class BlogForm(forms.ModelForm):

    content = MartorFormField()

    class Meta:
        model = Blog
        fields = ['content',]