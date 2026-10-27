from django.conf import settings
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('nome', max_length=100)
    description = models.TextField('descrição')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('título', max_length=200)
    content = models.TextField('conteúdo (HTML)')
    date = models.DateTimeField('data de postagem', default=timezone.now)
    categories = models.ManyToManyField(Category, blank=True, verbose_name='categorias')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='post')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='autor'
    )
    text = models.TextField('texto')
    date = models.DateTimeField('data de postagem', default=timezone.now)

    class Meta:
        ordering = ['-date']
        verbose_name = 'comentário'
        verbose_name_plural = 'comentários'

    def __str__(self):
        return f'{self.author} em "{self.post}"'