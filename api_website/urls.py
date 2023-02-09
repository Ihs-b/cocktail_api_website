from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('cocktails/', views.cocktails, name="api_website-cocktails"),
    path('random_drinks/', views.random_drinks, name="api_website-random_drinks"),
    path('login/', auth_views.LoginView.as_view(template_name="api_website/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

]