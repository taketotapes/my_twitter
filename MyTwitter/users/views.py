from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .models import User
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, FollowForm


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user-list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'


@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    is_following = request.user.userprofile.followers.filter(id=user.id).exists()
    follow_form = FollowForm()

    if request.method == 'POST':
        follow_form = FollowForm(request.POST, instance=request.user.userprofile)
        if follow_form.is_valid():
            followers = follow_form.cleaned_data.get('followers')
            if user in followers.all():
                request.user.userprofile.followers.remove(user)
            else:
                request.user.userprofile.followers.add(user)
            return redirect('user-profile', user_id=user.id)

    return render(request, 'users/user_profile.html', {'user': user, 'is_following': is_following, 'follow_form': follow_form})


@login_required
def edit_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', user_id=user.id)
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'users/edit_profile.html', {'user': user, 'form': form})


@login_required
def user_followers(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = UserProfile.objects.get(user=user)
    followers = user_profile.get_followers()
    return render(request, 'users/user_followers.html', {'user': user, 'following': followers})


@login_required
def user_following(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = UserProfile.objects.get(user=user)
    following = user_profile.get_following()
    return render(request, 'users/user_following.html', {'user': user, 'following': following})


@login_required
def follow_user(request, user_id):
    if request.method == 'POST':
        user_to_follow = User.objects.get(id=user_id)
        request.user.following.add(user_to_follow)
        return redirect('user-profile', args=[user_id])
    else:
        return HttpResponseRedirect(reverse('user-profile', args=[user_id]))
