from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()  # Використовуємо наш менеджер 'published' [cite: 325]
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post,  # Використовуємо get_object_or_404 для обробки помилок [cite: 342]
                             id=id,
                             status=Post.Status.PUBLISHED)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})