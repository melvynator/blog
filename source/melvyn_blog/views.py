from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def posts(request):
    all_posts = Post.objects.order_by('published_date')
    paginator = Paginator(all_posts, 2)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    return render(request, 'melvyn_blog/posts.html', context)

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'melvyn_blog/post.html', {'post': post})

def contact(request):
    return render(request, 'melvyn_blog/contact.html', {})

def about(request):
    return render(request, 'melvyn_blog/about.html', {})

def home(request):
    return render(request, 'melvyn_blog/home.html', {})
