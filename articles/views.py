from django.shortcuts import render
from django.views.generic import DetailView
from .models import Article

# Create your views here.

def ArticleListView(request):
    latest_list = Article.objects.order_by('-id')
    return render(request, 'blog.html', {"latest_list": latest_list})


class BlogDetailView(DetailView):
    model = Article
    template_name = 'single-blog.html'