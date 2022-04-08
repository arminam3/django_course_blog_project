from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields="__all__"


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"