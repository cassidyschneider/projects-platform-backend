from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.projects, name='projects'),
    path('all/public/', views.projects_public, name='projects_public'),
    path('user/', views.user, name='user'),
    path('add_project/', views.add_project, name='add_projects'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
