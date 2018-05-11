from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           max_length=3000,
                           label='你的想法')

    class Meta:
        model = Blog
        fields = ['content',]