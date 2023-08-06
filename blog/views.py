from django.shortcuts import render
from django.views import View

from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from .models import SocialMedia
from django.http import HttpResponse

def index(request):
    return HttpResponse('')
def post_study(request):
    return render(request, 'blog/post_study.html')

def telegram(request):
    return redirect("https://web.telegram.org/k/")
def vk(request):
    return redirect("https://vk.com/")

def whatsapp(request):
    return redirect('https://www.whatsapp.com/?lang=ru_RU')

def discord(request):
    return redirect('https://discord.com/')

def mail(request):
    return redirect('https://mail.ru/')


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_number(request, my_pk):
    post = get_object_or_404(Post,pk=my_pk)
    return render(request, 'blog/post_list.html', {'post': post})
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def socialmedia_link(request, pk):
    link = get_object_or_404(SocialMedia, pk)
    return redirect(request, 'blog/base.html', pk=link.pk)

