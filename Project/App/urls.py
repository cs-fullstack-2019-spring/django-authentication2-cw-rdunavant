from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_titles, name='blogTitle'),
    path('blog_entries/', views.blog_entries, name='blog_entries'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]