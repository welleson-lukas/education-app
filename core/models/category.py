from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    slug = models.SlugField('Slug', max_length=254, null=True, blank=True, unique=True)
    name = models.CharField('Name', max_length=254, null=False)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.name)}'
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"