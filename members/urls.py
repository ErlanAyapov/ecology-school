from django.urls import path
from . import views 


urlpatterns = [
    path('register/', views.UserRegisterView, name = 'register'),
    path('auth/', views.auth, name = 'auth'),
    path('logout/', views.logout, name = 'logout'),
    path('customer/', views.customer, name = 'customer'),
    path('<int:pk>/', views.UserUpdate.as_view(), name = 'update_user')
]
