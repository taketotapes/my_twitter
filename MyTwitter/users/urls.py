from django.urls import path
from .views import UserListView, user_profile, edit_profile, user_following, user_followers, follow_user, home, register
from .views import login_user, logout_user

urlpatterns = [
    path('', home, name='home'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:user_id>/', user_profile, name='user-profile'),
    path('users/<int:user_id>/edit/', edit_profile, name='edit-profile'),
    path('users/<int:user_id>/followers/', user_followers, name='user-followers'),
    path('users/<int:user_id>/following/', user_following, name='user-following'),
    path('users/follow/<int:user_id>/', follow_user, name='follow'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]