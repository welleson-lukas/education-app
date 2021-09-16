from django.db import models
from core.models.author import Author
from core.models.post import Post


class Comment(models.Model):
    comment = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Usuário', related_name='comment_author',
                                blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Publicação', related_name='comment_post',
                             blank=True, null=True)
    publish = models.BooleanField('Publicado?', null=False, default=False)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.author.user.username