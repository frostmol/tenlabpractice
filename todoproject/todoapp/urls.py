from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register', views.register, name = 'register'),
    path('login', views.loginuser, name = 'login'),
    path('logout/', views.logoutView, name ='logout'),
    path('delete-task/<str:name>/', views.DeleteTask, name ='delete'),
    path('update/<str:name>/', views.Update, name ='update'),
]
