from django.urls import path
from . import views

urlpatterns = [
    path('postlist/', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/postdetail/', views.PostDetailView.as_view(), name='post_detail'),
    path('newpost/', views.PostCreateView.as_view(), name='new_post'),
    path('<int:pk>/updatepost/', views.PostUpdateView.as_view(), name='update_post'),
    path('<int:pk>/deletepost/', views.PostDeleteView.as_view(), name='delete_post'),
]
