from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('home_page', views.home_page, name='home_page'),
    path('about_page', views.about_page, name='about_page'),
]