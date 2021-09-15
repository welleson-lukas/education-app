from django.shortcuts import render
from core.models.author import Author


def teste(request, template_name='teste.html'):
    autor = Author.objects.get(user=request.user)
    return render(request, template_name, {'autor':autor})