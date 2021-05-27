from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, ArticleUpdateForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
import datetime
from django.urls import reverse_lazy
# from circle.models import Group

class MainView(ListView):
	model = Article
	ordering = '-date'
	template_name = 'main/index.html'
	# def get_context_data(self, **kwargs):
	# 	context = super(DetailsView, self).get_context_data(**kwargs)
	# 	context['groups'] = Group.objects.all()
	# 	return context

def article_add(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			form.date = datetime.datetime.now()
			form.save()
			return redirect('home')

	form = ArticleForm()
	data = {
		'news_form':form,
	}
	return render(request, 'main/add.html', data)

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'main/detail.html'

class ArticleDeleteView(DeleteView):
	model = Article
	template_name = 'main/delete.html'
	success_url = reverse_lazy('home')


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'main/update.html'
    # fields = ['title', 'slug', 'body', 'image']
    def form_valid(self, form):
        form.save()
        return redirect('home')