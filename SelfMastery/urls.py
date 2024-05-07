# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),
]
