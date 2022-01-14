from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs_view(request):
    blogs = Blog.objects.all()
    # blogs = Blog.objects.order_by('-date')
    latest_blogs = Blog.objects.order_by('-date')[:4]
    blog_count = Blog.objects.count()
    # blogs = Blog.objects.filter(date="2021-11-23")
    context = {
        'blogs': blogs,
        'latest_blogs': latest_blogs,
        'blog_count': blog_count
    }
    return render(request, 'blog/all_blogs.html', context)


def blog_detail_view(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog_detail.html', context)
