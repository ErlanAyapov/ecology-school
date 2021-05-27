from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, EmailInput
from .models import Customer


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2' )
 
class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name')
		widgets = {
			'email': 	  TextInput(attrs={'class': 'form-control','placeholder': 'почта',}),
			'first_name': TextInput(attrs={'class': 'form-control','placeholder': 'Есімі',}),
			'last_name':  TextInput(attrs={'class': 'form-control','placeholder': 'Тегі',}),
			}


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('birth_day','birth_mounth', 'birth_year', 'circle', 'user')
		exclude = ['user']
