from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ArticleViewSet, ArticlesFavoriteAPIView, ArticlesFeedAPIView,
    CommentsListCreateAPIView, CommentsDestroyAPIView, TagListAPIView
)

app_name = 'articles'

router = DefaultRouter(trailing_slash=False)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('articles/feed', ArticlesFeedAPIView.as_view()),
    path('articles/<article_slug>/favorite', ArticlesFavoriteAPIView.as_view()),
    path('articles/<article_slug>/comments/', CommentsListCreateAPIView.as_view()),
    path('articles/<articles_slug>/comments/<comments_pk>', CommentsDestroyAPIView.as_view()),
    path('tags', TagListAPIView.as_view()),
]

urlpatterns += router.urls

# urlpatterns = [
#     url(r'^', include(router.urls)),

#     url(r'^articles/feed/?$', ArticlesFeedAPIView.as_view()),

#     url(r'^articles/(?P<article_slug>[-\w]+)/favorite/?$',
#         ArticlesFavoriteAPIView.as_view()),

#     url(r'^articles/(?P<article_slug>[-\w]+)/comments/?$',
#         CommentsListCreateAPIView.as_view()),

#     url(r'^articles/(?P<article_slug>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$',
#         CommentsDestroyAPIView.as_view()),

#     url(r'^tags/?$', TagListAPIView.as_view()),
# ]