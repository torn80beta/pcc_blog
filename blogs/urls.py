from django.urls import path
from . import views

"""Определение схемы URL для проекта"""
app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # New post page
    path('new_post/', views.new_post, name='new_post'),
]

