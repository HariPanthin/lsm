from django.urls import path
from front import views
urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('funding/', views.funding, name='funding'),
    path('resources/', views.resources, name='recources'),
]

