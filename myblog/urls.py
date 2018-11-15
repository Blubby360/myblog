from django.urls import path
from . import views

app_name = 'myblog'

urlpatterns = [
	path('', views.home, name = 'home'),
    path('posts/', views.posts_index, name = 'posts_index'),
    path('posts/<int:post_id>/', views.posts_show, name = 'posts_show'),
    path('authors/', views.authors_index, name = 'authors_index'),
    path('authors/<int:author_id>', views.authors_show, name = 'authors_show'),
]