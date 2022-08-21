from django.urls import path
from . import views

"""Определение схемы URL для проекта"""
app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # New post page
    path('new_post/', views.new_post, name='new_post'),
    # Single post page
    path('posts/<int:post_id>/', views.post, name='post'),
    # Edit page
    path('edit_entry/<int:post_id>', views.edit_entry, name='edit_entry'),
]

