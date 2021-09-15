from django.contrib import admin
from core.models.post import Post
from core.models.author import Author
from core.models.category import Category
from core.models.tag import Tag
from core.models.file import File
from core.forms.post_form import PostForm
from core.forms.category_form import CategoryForm


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish', 'author', 'created_at', 'updated_at', 'slug']
    search_fields = ('title',)
    list_editable = ['publish']
    list_filter = ('publish', 'author', 'categories')
    form = PostForm

    fieldsets = [
        ("Título e publicação", {'fields': (tuple(['title', 'publish']),), }),
        ("Imagem", {'fields': ['image']}),
        ("Excerto", {'fields': ['excerpt']}),
        ("Conteúdo", {'fields': ['content']}),
        ("Categorias", {'fields': ['categories']}),
        ("Tags", {'fields': ['tags']}),
    ]

    def save_model(self, request, obj, form, change):
        autor = Author.objects.get(user=request.user)
        print(autor)
        obj.author = autor
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )
    form = CategoryForm


admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)