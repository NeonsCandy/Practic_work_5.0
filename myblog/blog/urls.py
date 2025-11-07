from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # URL для списку постів (головна сторінка)
    path('', views.post_list, name='post_list'),
    # URL для детальної сторінки поста
    path('<int:id>/', views.post_detail, name='post_detail'),
]