from django.shortcuts import render, redirect
from .models import Post, Comment, Article
from .forms import PostForm, ArticleUpdateForm, CommentForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
import datetime
from django.urls import reverse_lazy
# from circle.models import Group

class MainView(ListView):
	model = Post
	ordering = '-date'
	template_name = 'main/index.html'

	# def get_context_data(self, **kwargs):
	# 	context = super(MainView, self).get_context_data(**kwargs)
	# 	context['comment'] = Comment.objects.all()
	# 	return context

def article_add(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			form.date = datetime.datetime.now()
			form.save()
			return redirect('home')

	form = PostForm()
	data = {
		'news_form':form,
	}
	return render(request, 'main/add.html', data)



class ArticleDetailView(DetailView):
	model = Post
	template_name = 'main/detail.html'

class ArticleDeleteView(DeleteView):
	model = Post
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



def CommentAddView(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			form = form.save(commit = False)
			form.author = request.user
			form.save()
			return redirect('home')

	form = CommentForm()
	data = {
		'comment_form':form,
	}

	return render(request, 'main/comment.html', data)