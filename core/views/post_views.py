from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from core.models.comment import Comment
from core.models.post import Post


def post_view(request, slug):
    # post_p = Post.objects.get(slug=post, publish=True)
    post_p = get_object_or_404(Post, slug=slug, publish=True)

    comments = Comment.objects.filter(publish=True, post=post_p)
    for i in comments:
        print(i.author)
    context = {
        'post': post_p,
        'comentarios': comments
    }
    return render(request, 'core/post.html', context)
