from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'ingredients', 'instructions', 'preparation_time', 'cooking_time', 'serves')