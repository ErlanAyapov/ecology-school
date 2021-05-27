from django.shortcuts import render, redirect
from .forms import UserCreateForm, CustomerForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as django_logout
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.models import User
from circle.models import Group


def UserRegisterView(request):
	error = ''
	if request.method == 'POST':
		form = UserCreateForm(request.POST)

		if form.is_valid():
			form.save() 
			username = request.POST.get('username')  
			password = request.POST.get('password1') 
			user = authenticate(request, username = username, password = password)

			if user is not None: 
				login(request, user)
				return HttpResponseRedirect('/user/' + str(request.user.id) + '/') 

		else:
			error = 'Логин бос емес немесе құпия сөздер сәйкес емес!'
			context = {
				'register_form':form,
				'message':error,
			}
			return render(request, 'members/register.html', context)

	else:
		form = UserCreateForm()
  
	return render(request, 'members/register.html', {'register_form':form})

def auth(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = 'Қолданушы атауы немесе құпия сөз дұрыс емес!'
            return render(request, 'members/auth.html', {'error':error})
    return render(request, 'members/auth.html')


def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')

def customer(request):
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			form.save()
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('Дұрыс толтырылмады!')

	form = CustomerForm()
	customer = Group.objects.all()
	data = {
	'form':form,
	'day':range(1, 32, 1),
	'mounth':range(1, 13, 1),
	'year':range(2013, 1900, -1),
	'customer':customer,
	}

	return render(request, 'custome/custome.html', data)


class UserUpdate(UpdateView):
	model = User
	form_class = UserUpdateForm
	template_name = 'user/update.html'
    # fields = ['title', 'slug', 'body', 'image']
	def form_valid(self, form):
		form.save()
		return redirect('customer')
