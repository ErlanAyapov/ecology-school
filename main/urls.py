from django.urls import path
from . import views 


urlpatterns = [
    path('', views.MainView.as_view(), name = 'home'),
    path('add/', views.article_add, name = 'add'),
    path('detail/<int:pk>/', views.ArticleDetailView.as_view(), name = 'article_detail'),
    path('delete/<int:pk>/', views.ArticleDeleteView.as_view(), name = 'delete_article'),
    path('update/<int:pk>>', views.ArticleUpdateView.as_view(), name = 'update')

]
