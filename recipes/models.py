from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    preparation_time = models.IntegerField(help_text="準備時間（分）")
    cooking_time = models.IntegerField(help_text="調理時間（分）")
    serves = models.IntegerField(help_text="何人分")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name