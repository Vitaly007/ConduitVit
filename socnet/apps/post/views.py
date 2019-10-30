from rest_framework.viewsets import ModelViewSet

from .models import Post, PostLike
from .serializers import PostSerializer, PostLikeSerializer

# Create your views here.


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(**{'owner': self.request.user})

    def perform_update(self, serializer):
        serializer.save(**{'owner': self.request.user})


class PostLikeViewSet(ModelViewSet):

    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

    def perform_create(self, serializer):
        serializer.save(**{
            'user': self.request.user,
            'post_id': int(self.kwargs['post_id'])
        })

    def perform_update(self, serializer):
        serializer.save(**{
            'user': self.request.user,
            'post_id': int(self.kwargs['post_id'])
        })
