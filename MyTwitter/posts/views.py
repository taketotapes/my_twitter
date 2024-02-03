from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from .models import Post, Comment, User
from .forms import PostForm


def home(request):
    return render(request, 'posts/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post-list')
        else:
            form = UserCreationForm()
        return render(request, 'posts/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post-list')
    else:
        form = AuthenticationForm()
    return render(request, 'posts/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('post-list')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post-list')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {'form': form}, {'post': post})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')

    return render(request, 'posts/delete_post.html', {'post': post})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    liked = False
    comments = Comment.objects.filter(post=post)
    if request.method == "POST":
        action = request.POST.get('action')
        if action == 'like':
            post.likes.add(request.user)
            liked = True
        elif action == 'unlike':
            post.likes.remove(request.user)

    return render(
        request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'liked': liked},
    )


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def comments_for_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'posts/comments_for_post.html', {'post': post, 'comments': comments})


def user_list(request, user_id):
    users = User.objects.all()
    return render(request, 'posts/user_list.html', {'users': users})


def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'posts/user_detail.html', {'user': user})


def posts_for_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user=user)
    return render(request, 'posts/posts_for_user.html', {'user': user, "posts": posts})