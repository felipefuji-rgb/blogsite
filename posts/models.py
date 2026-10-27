from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField('título', max_length=200)
    content = models.TextField('conteúdo (HTML)')
    date = models.DateTimeField('data de postagem', default=timezone.now)

    def __str__(self):
        return self.title