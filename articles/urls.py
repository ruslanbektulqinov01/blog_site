from django.urls import path
from articles.views import article_all




urlpatterns = [
    path('', article_all, name='article_all'),
]