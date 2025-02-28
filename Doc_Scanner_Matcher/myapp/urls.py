from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.user_login, name='login'),
    path('', views.home, name='home'),
]