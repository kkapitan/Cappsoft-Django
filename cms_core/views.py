from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from registration.backends.simple.views import RegistrationView

from .models import Post, Project
from .forms import PostForm



def post_list(request):
    posts = Post.objects.order_by('published_date')

    return render(request, 'blog/index.html', {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/show.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/new.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit.html', {'form': form})


def home(request):
    projects = Project.objects.all()

    return render(request, 'home.html', {'projects': projects})


def user_list(request):
    users = User.objects.all()

    return render(request, 'users/index.html', {'users': users })


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author_id=user.id)

    return render(request, 'users/show.html', {'user': user, 'posts': posts})


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return "/blog"