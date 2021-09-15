import uuid
import os

from django.db import models
from core.models.post import Post


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("documents", filename)


class File(models.Model):
    title = models.CharField('Title', max_length=200)
    file = models.FileField(upload_to=get_file_path, null=True, verbose_name='File')
    created_at = models.DateTimeField('Created_at', auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='File', related_name='files')

    def __str__(self):
        return self.title