from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from melvyn_blog.forms import ContactForm
from django.template.loader import get_template
from django.template import Context
from .models import Post
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


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
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            template = get_template('contact_template.txt')
            context = Context({'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)
            send_mail(contact_name, content, contact_email, ['peignonmel@eisti.eu'], fail_silently=False)
            return HttpResponseRedirect("#")

    return render(request, 'melvyn_blog/contact.html', {'form': form_class, })


def about(request):
    return render(request, 'melvyn_blog/about.html', {})


def home(request):
    return render(request, 'melvyn_blog/home.html', {})
