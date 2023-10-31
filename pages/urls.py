from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('performer/', PerformerPageView.as_view(), name='performer'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('blog/', BlogPageView.as_view(), name='blog'),
]