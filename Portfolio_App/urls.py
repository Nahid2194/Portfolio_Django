from django.urls import path
from Portfolio_App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-form/', views.admin_form, name='admin_form'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('add-skills/', views.add_skills, name='add_skills'),
    path('add-project/', views.add_project, name='add_project'),
    path('add-portfolio/', views.add_portfolio, name='add_portfolio'),
]
