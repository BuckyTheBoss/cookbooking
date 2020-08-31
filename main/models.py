from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    sp_id = models.IntegerField()
    image = models.URLField()
    servings = models.IntegerField()
    summary = models.CharField(max_length=50)


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

