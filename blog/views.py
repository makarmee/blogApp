from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def starting_page(request):
  latestPosts=Post.objects.all().order_by('-date')[:3]
  return render(request,'blog/index.html',{
    'posts':latestPosts
  })

def posts(request):
  allPosts=Post.objects.all().order_by('-date')
  return render(request,'blog/all-posts.html',{
    'all_posts':allPosts
  })

def post_detail(request,slug):
  identifiedPost=get_object_or_404(Post,slug=slug)
  return render(request,'blog/post-detail.html',{
    'post':identifiedPost,
    'post_tags':identifiedPost.tags.all()
    })