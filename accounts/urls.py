from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('about/', views.about, name = 'about'),
    path('terms/', views.terms, name = 'terms'),
    path('contact/', views.contact, name = 'contact'),
    
    path('client/<str:ID>/', views.client, name='client'),
    path('broker/<str:ID>/', views.broker, name='broker'),
]

