from django.shortcuts import render

from yoi_app.models import Post


def index(request):
    posts = get_posts()
    return render(request, 'index.html', {'posts': posts})


def get_posts():
    return Post.objects.order_by('id')
