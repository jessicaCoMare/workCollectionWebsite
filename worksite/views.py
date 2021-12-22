from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
import markdown
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("欢迎访问我的博客.")
    post_list = Post.objects.all().order_by('-created_time')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(post_list,5,1)

    try:
        num = request.GET.get('index', '1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'post_list':post_list, 'categories':categories, 'tags':tags, 'page':number, 'paginator':paginator})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_list = Post.objects.all().order_by('-created_time')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    post.body = markdown.markdown(post.body,
                                    extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                    ])
    return render(request, 'blog/detail.html',{'post':post, 'post_list':post_list, 'categories':categories, 'tags':tags})

def search_category(request, category):
    post_list = Post.objects.filter(category__name=category)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(post_list,5,1)

    try:
        num = request.GET.get('index', '1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'post_list':post_list, 'categories':categories, 'tags':tags, 'page':number, 'paginator':paginator})

def search_tag(request, tag):
    post_list = Post.objects.filter(tags__name=tag)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(post_list,5,1)

    try:
        num = request.GET.get('index', '1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'post_list':post_list, 'categories':categories, 'tags':tags, 'page':number, 'paginator':paginator})
