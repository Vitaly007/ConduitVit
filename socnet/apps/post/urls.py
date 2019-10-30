from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, PostLikeViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, base_name='api-post')
router.register(
    'posts/(?P<post_id>[0-9]+)/likes',
    PostLikeViewSet,
    base_name='api-post-like')

urlpatterns = [
    path('', include(router.urls)),
]
