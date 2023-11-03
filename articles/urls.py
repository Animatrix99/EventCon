from django.urls import path
from .views import ArticleListView, BlogDetailView


urlpatterns = [
    path('', ArticleListView, name='blog'),
    path('<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]