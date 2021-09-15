from django.shortcuts import render
from django.views.generic import DetailView
from core.models.post import Post


class PostView(DetailView):
    model = Post
    template_name = 'core/index.html'
    #template_name = 'core/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(publish=True)

        return qs