from django.urls import path
from account import views

urlpatterns = [
    path('dashboard', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    
]