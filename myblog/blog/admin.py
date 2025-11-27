from django.contrib import admin
from .models import Post, Comment

# 1. Налаштування для ПОСТІВ
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Поля саме моделі Post
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

# 2. Налаштування для КОМЕНТАРІВ
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Поля саме моделі Comment
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']