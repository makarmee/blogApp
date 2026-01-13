from datetime import date
from django.shortcuts import render

allPosts=[{
  'slug':'hike-in-the-mountian',
  'image':'mountain.png',
  'author':'mahdi',
  'date':date(2025,1,5),
  'title':'Mountain Hiking',
  'excerpt':"There is nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoting the view.",
  'content':"""
  Lorem, ipsum dolor sit amet consectetur adipisicing elit. Excepturi est iusto natus maxime corporis veritatis perferendis optio error adipisci ad laborum, quas esse, quo et? Qui consequatur consectetur quia quam.
  
  Lorem, ipsum dolor sit amet consectetur adipisicing elit. Excepturi est iusto natus maxime corporis veritatis perferendis optio error adipisci ad laborum, quas esse, quo et? Qui consequatur consectetur quia quam.
  
  Lorem, ipsum dolor sit amet consectetur adipisicing elit. Excepturi est iusto natus maxime corporis veritatis perferendis optio error adipisci ad laborum, quas esse, quo et? Qui consequatur consectetur quia quam.
  """
},{
  'slug':'into-the-woods',
  'image':'wood.png',
  'author':'mahdi',
  'date':date(2025,1,7),
  'title':'Nature At its Best!',
  'excerpt':"Dolor cupidatat consequat duis reprehenderit sit aute aliqua sint officia.",
  'content':"""
  Lorem, ipsum dolor sit amet consectetur adipisicing elit. Excepturi est iusto natus maxime corporis veritatis perferendis optio error adipisci ad laborum, quas esse, quo et? Qui consequatur consectetur quia quam.
  
  Lorem, ipsum dolor sit amet consectetur adipisicing elit. Excepturi est iusto natus maxime corporis veritatis perferendis optio error adipisci ad laborum, quas esse, quo et? Qui consequatur consectetur quia quam.
  
  Lorem, ipsum dolor sit amet consectetur adipisicing elit. Excepturi est iusto natus maxime corporis veritatis perferendis optio error adipisci ad laborum, quas esse, quo et? Qui consequatur consectetur quia quam.
  """
},{
  'slug':'programming-is-fun',
  'image':'coding.png',
  'author':'mahdi',
  'date':date(2025,1,5),
  'title':'Programming is Great!',
  'excerpt':"Mollit incididunt ullamco id sint et fugiat adipisicing eu sunt proident dolore magna mollit.",
  'content':"""
  Lorem, ipsum dolor sit amet consectetur adipisicing elit. Excepturi est iusto natus maxime corporis veritatis perferendis optio error adipisci ad laborum, quas esse, quo et? Qui consequatur consectetur quia quam.
  
  Lorem, ipsum dolor sit amet consectetur adipisicing elit. Excepturi est iusto natus maxime corporis veritatis perferendis optio error adipisci ad laborum, quas esse, quo et? Qui consequatur consectetur quia quam.
  
  Lorem, ipsum dolor sit amet consectetur adipisicing elit. Excepturi est iusto natus maxime corporis veritatis perferendis optio error adipisci ad laborum, quas esse, quo et? Qui consequatur consectetur quia quam.
  """
}]


def get_date(post):
  return post['date']

# Create your views here.
def starting_page(request):
  sortedPosts=sorted(allPosts,key=get_date)
  latestPosts=sortedPosts[-3:]
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