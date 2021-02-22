from django.urls import path
from Portfolio_App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-login/', views.admin_login, name='admin_login'),
]
