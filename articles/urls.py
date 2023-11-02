from django.urls import path
from .views import ArticleListView


urlpatterns = [
    path('blog/', ArticleListView.as_view(), name='blog')
]