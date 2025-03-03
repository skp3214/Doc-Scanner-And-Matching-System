from django.urls import path
from . import views


urlpatterns = [
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.user_login, name='login'),
    path('', views.home, name='home'),
    path('user/profile/', views.profile, name='profile'),
    path('credits/request/', views.request_credits, name='request_credits'),
    path('credits/admins', views.admin_credits, name='admin_credits'),
    path('scan/', views.scan_document, name='scan_document'),  
    path('matches/<int:doc_id>/', views.matches, name='matches'),
    path('document/<int:doc_id>/', views.document_detail, name='document_detail'),
    path('download-scan-history/', views.download_scan_history, name='download_scan_history'), 
    path('admins/analytics/', views.analytics, name='analytics'),
    path('logout/', views.user_logout, name='logout'),
]