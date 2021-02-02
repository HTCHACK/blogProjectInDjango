from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.forms.fields import SlugField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from blogapp.models import Category, News, Post
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView
from .forms import *


# Create your views here.

class CatListView(ListView):
    template_name = 'store/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = { 
        'cat': self.kwargs['category'],
        'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status=1)
        }
        return content

def category_list(request):
    category_list = Category.objects.exclude()
    context = {'category_list':category_list}
    return context

def single_post(request,slug):
    # Comment posted
    post = Post.objects.get(slug=slug)
    comments = BlogComment.objects.order_by('-created_on').filter(post=post)
    user_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = CommentForm()
    

    context = {'post': post, 'comments':  user_comment, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'store/single_post.html', context)


def index(request):
    categories = Category.objects.all()
    category_list = Category.objects.exclude(name='default')
    posts = Post.objects.all().order_by('-created_on')
    comments = BlogComment.objects.filter() 
    context = {'posts': posts,'categories': categories,'comments':comments,'category_list': category_list,}
    return render(request, 'store/index.html', context)


def news(request):
    categories = Category.objects.all()
    category_list = Category.objects.exclude(name='default')
    posts = Post.objects.order_by('-created_on')[:3]
    news = News.objects.order_by('-created_on')

    form_subs = SubscribeForm()

    if request.method == 'POST':
        form_subs = SubscribeForm(request.POST)
        if form_subs.is_valid():
            form_subs.save()
            return HttpResponseRedirect(reverse('store:news'))
    context = {'news': news,'form_subs':form_subs,'categories': categories,'posts':posts,'category_list': category_list,}
    return render(request, 'store/news.html', context)


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('store:index'))

    context = {'form': form}
    return render(request, 'store/contact.html', context)


