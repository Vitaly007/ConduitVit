from django.db import models
from django_extensions.db.models import TimeStampedModel

#from django_hstore import hstore


from socnet.apps.authentication.models import User

# from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your models here.


class Post(TimeStampedModel):
    owner = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    description = models.TextField()
    post = models.TextField() #hstore.DictionaryField()

    #objects = hstore.HStoreManager()

    class Meta:
        db_table = 'user_post'
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return '{}'.format(self.post)


class PostLike(TimeStampedModel):
    user = models.ForeignKey(
        User, related_name='post_likes', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE)
    like = models.BooleanField()

    class Meta:
        db_table = 'user_post_like'
        verbose_name = "Post Like"
        verbose_name_plural = "Post Likes"
        unique_together = ("user", "post")
