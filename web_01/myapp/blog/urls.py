from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_id>/', views.detail, name='blog_detail'),
]