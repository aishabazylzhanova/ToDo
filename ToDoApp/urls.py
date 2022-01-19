from django.urls import path
from . import views
from .views import TasksView
from .views import  Login, Register
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('', TasksView.as_view(), name='tasks'),
    path('create/', views.create, name='create'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
]