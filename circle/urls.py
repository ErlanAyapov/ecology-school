from django.urls import path
from . import views

urlpatterns = [
	path('', views.GroupView.as_view(), name = 'group'),
	path('<int:pk>/', views.DetailsView.as_view(), name = 'detail'),
]