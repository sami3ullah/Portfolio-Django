from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    blog = Blog.objects
    return render(request, 'Blog/blog.html', {'blog': blog})

def blog_detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'Blog/blog_detail.html', {'blog_detail': blog_detail})
