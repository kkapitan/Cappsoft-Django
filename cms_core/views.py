from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'index.html', {"posts": posts})