from django.shortcuts import render, redirect
import recipe_api as ra
from .models import Recipe, Ingredient
from django.contrib.auth.decorators import login_required


# Create your views here.

def homepage(request):
    items = []
    if request.method == 'POST':
        text = request.POST.get('search')
        items = ra.search(text)

    return render(request, 'search.html', {'items': items} )


def recipe_info(request, recipe_id):
    recipe_dict = ra.get_by_id(recipe_id)
    recipe, created = Recipe.objects.get_or_create(
        title=recipe_dict["title"],
        sp_id=recipe_dict["id"],
        image=recipe_dict['image'],
        servings=recipe_dict['servings'],
        summary=recipe_dict['summary']
    )
    if created:
        for ingredient in recipe_dict['extendedIngredients']:
            ing = Ingredient.objects.create(
                name=ingredient['name'],
                amount=ingredient['measures']['metric']['amount'],
                recipe=recipe
            )

    return render(request, 'single_recipe.html', {'recipe': recipe})


@login_required
def add_to_my_recipes(request, id):
    recipe = Recipe.objects.get(id=id)
    request.user.profile.recipes.add(recipe)
    return redirect('my_recipes')


@login_required
def my_recipes(request):
    return render(request, 'my_recipes.html')
