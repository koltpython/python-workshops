from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post

# Create your views here.

# index view
def index(request):
    all_posts = Post.objects.all()

    posts_data = {
        # we'll access all post with 'posts' name.
        'posts': all_posts
    }

    return render(request, 'blog/index.html', context=posts_data)



def post_detail(request, pk):
    selected_post = Post.objects.get(pk=pk)

    posts_data = {
        'post_in_detail': selected_post
    }

    return render(request, 'blog/post_detail.html', context=posts_data)