from django.apps import AppConfig


class ArticlesAppConfig(AppConfig):
    name = 'socnet.apps.articles'
    label = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        import socnet.apps.articles.signals

default_app_config = 'socnet.apps.articles.ArticlesAppConfig'
