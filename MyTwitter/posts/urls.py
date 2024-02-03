from django.urls import path
from .views import home, post_list, post_detail, comments_for_post, user_list, user_detail, posts_for_user
from .views import register, login_user, logout_user, create_post, edit_post, delete_post

urlpatterns = [
    path('', home, name='home'),
    path('posts/', post_list, name='post-list'),
    path('posts/<int:post_id>/', post_detail, name='post-detail'),
    path('posts/<int:post_id>/comments/', comments_for_post, name='comments-for-post'),
    path('users/', user_list, name='user-list'),
    path('users/<int:user_id>/', user_detail, name='user-detail'),
    path('users/<int:user_id>/posts/', posts_for_user, name='posts-for-user'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-post/', create_post, name='create-post'),
    path('posts/<int:post_id>/edit/', edit_post, name='edit-post'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete-post'),
]