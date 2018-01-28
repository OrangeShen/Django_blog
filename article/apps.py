from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class ArticleConfig(AppConfig):
    name = 'article'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'