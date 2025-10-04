from django.urls import path
from .views import register_view, CustomLoginView, CustomLogoutView, profile, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Auth routes
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
] 
