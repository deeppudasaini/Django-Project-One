from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home,name="Home"),
    path('home', views.home,name="Home"),
    path('login', views.login,name="login"),
    path('logout', views.logout,name="logout")
]