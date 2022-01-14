from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs_view, name='all_blogs'),
    path('<int:blog_id>/', views.blog_detail_view, name='blog_detail'),
]