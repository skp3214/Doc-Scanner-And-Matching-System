from django.urls import path
from . import views


urlpatterns = [
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.user_login, name='login'),
    path('', views.home, name='home'),
    path('user/profile/', views.profile, name='profile'),
    path('credits/request/', views.request_credits, name='request_credits'),
    path('credits/admins', views.admin_credits, name='admin_credits'),
]