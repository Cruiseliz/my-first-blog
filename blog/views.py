from django.shortcuts import render
from django.utils import timezone
# 同じディレクトリないのファイル同士は.をつけるだけで表記することができる。
from .models import POST

# Create your views here.

def post_list(request):
    posts = POST.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {
    'posts':posts
    })
