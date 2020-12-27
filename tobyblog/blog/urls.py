from django.urls import path
from .views import PostListView, PostDetialView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name="blog-index"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('blog/<int:pk>/', PostDetialView.as_view(), name="blog-detial"),
    path('blog/create/', PostCreateView.as_view(), name="blog-create"),
    path('login/', views.login, name="blog-login"),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name="blog-update"),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name="blog-delete"),
    path('about/', views.about, name="blog-about"),
]

