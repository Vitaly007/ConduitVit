from socnet.apps.core.renderers import SocnetJSONRenderer


class ArticleJSONRenderer(SocnetJSONRenderer):
    object_label = 'article'
    pagination_object_label = 'articles'
    pagination_count_label = 'articlesCount'


class CommentJSONRenderer(SocnetJSONRenderer):
    object_label = 'comment'
    pagination_object_label = 'comments'
    pagination_count_label = 'commentsCount'