from django import forms
from core.models.category import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput()
        }

        help_texts = {
            'name': 'Um nome para a category'
        }