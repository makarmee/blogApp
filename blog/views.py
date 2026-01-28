from datetime import date
from django.shortcuts import render
from .models import Post


allPosts=[]


def get_date(post):
  return post['date']

# Create your views here.
def starting_page(request):
  latestPosts=Post.objects.all().order_by('-date')[:3]
  return render(request,'blog/index.html',{
    'posts':latestPosts
  })

def posts(request):
  return render(request,'blog/all-posts.html',{
    'all_posts':allPosts
  })

def post_detail(request,slug):
  identifiedPost=next(post for post in allPosts if post['slug']==slug)
  return render(request,'blog/post-detail.html',{'post':identifiedPost})