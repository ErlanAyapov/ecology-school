from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, EmailInput
from .models import Article, Comment, Post





class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author','body', 'date', 'youtube_link', 'image_base64')
		exclude = ['author', 'date']


class ArticleUpdateForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['body']
		widgets = {
			'body':  Textarea (attrs={'class': 'form-control', 'placeholder': 'Жаз...'}),
		}


class CommentForm(ModelForm):
	class Meta:

		model = Comment
		fields = ('author', 'post', 'comment')

		widgets = {
			'comment': Textarea(attrs = {'class': 'form-control'})
		}

		exclude = ['author']