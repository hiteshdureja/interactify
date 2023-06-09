from django.conf.urls import url
from django.urls import path

from news_feed.views.news_feeds import news_feed
from news_feed.views.likes import likes

urlpatterns = [
    path("", news_feed, name='feed'),
    path("likes/", likes),
]
