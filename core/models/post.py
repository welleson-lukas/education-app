import random
import uuid
import os

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.contrib.auth.models import User
from core.models.author import Author
from core.models.category import Category
from core.models.tag import Tag

def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("posts", filename)


class Post(models.Model):
    slug = models.SlugField('Slug', max_length=254, null=True, blank=True, unique=True)
    title = models.CharField('Título', max_length=254, null=False)
    content = RichTextUploadingField('Conteúdo', null=False)
    excerpt = models.TextField(verbose_name='Excerto')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Autor', related_name='post_author'
                               , blank=True, null=True)
    image = models.ImageField('Imagem', upload_to=get_file_path, blank=True, null=True)
    publish = models.BooleanField('Publicado?', null=False, default=False)

    categories = models.ManyToManyField(Category, related_name='post_categories')
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name='post_tag')

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    like = models.ManyToManyField(User, default=None, related_name='post_like')

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.title)}{str(random.randint(1, 200))}'
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_like(self):
        return self.like.all()

    @property
    def like_counts(self):
        return self.like.all().count()

    def get_user_like(self, user):
        pass

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Posts"