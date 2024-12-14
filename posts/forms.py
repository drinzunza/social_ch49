from django import forms
from .models import Post, Reactions, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image', 'video']
        labels = {
            'video' : 'Video URL'
        }


class ReactionForm(forms.ModelForm):
    class Meta:
        model = Reactions
        fields = ['react_type']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']