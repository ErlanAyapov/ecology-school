from django.shortcuts import render
from .models import Group
from django.views.generic import ListView, DetailView #, DeleteView, UpdateView
from main.models import Article
from members.models import Customer


class GroupView(ListView):
	model = Group
	template_name = 'circle/group.html'


class DetailsView(DetailView):
	model = Group
	template_name = 'circle/details.html'

	def get_context_data(self, **kwargs):
		context = super(DetailsView, self).get_context_data(**kwargs)
		context['article'] = Article.objects.all()
		context['customer'] = Customer.objects.all()
		return context