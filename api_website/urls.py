from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ChrabCreateView


urlpatterns = [
    path('', views.home, name="home"),
    path('cocktails/', views.cocktails, name="api_website-cocktails"),
    path('random_drinks/', views.random_drinks, name="api_website-random_drinks"),
    path('add_drinks/', ChrabCreateView.as_view(), name='add_drinks'),
]