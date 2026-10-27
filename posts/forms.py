from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'size': 60}),
            'content': forms.Textarea(attrs={'rows': 12, 'cols': 60}),
        }