from django.urls import path
from .views import ArticleListView


urlpatternes = [
    path('blog/', ArticleListView.as_view(), name='article_list')
]