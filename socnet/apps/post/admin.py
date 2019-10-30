from django.contrib import admin
from .models import Post, PostLike


class StaffAllowedAdmin:
    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True


class PostAdmin(StaffAllowedAdmin, admin.ModelAdmin):
    model = Post
    list_display = ('id', 'owner', 'post', 'likes', 'dislikes', 'created',
                    'modified')
    exclude = ('owner', )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)

    def likes(self, obj):
        return obj.likes.filter(like=True).count()

    def dislikes(self, obj):
        return obj.likes.filter(like=False).count()


class PostLikeAdmin(StaffAllowedAdmin, admin.ModelAdmin):
    model = PostLike
    list_display = ('id', 'post', 'user', 'like', 'created', 'modified')
    exclude = ('user', )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(PostLike, PostLikeAdmin)
