from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, EmailInput
from .models import Article





class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('author','body', 'group', 'date')
		exclude = ['author', 'date']


class ArticleUpdateForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['body']
		widgets = {
			'body':  Textarea (attrs={'class': 'form-control', 'placeholder': 'Жаз...'}),
		}