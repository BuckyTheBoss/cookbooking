from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('show_recipe/<int:recipe_id>', views.recipe_info, name="show_recipe"),
    path('add_recipe/<int:id>', views.add_to_my_recipes, name='add_recipe'),
    path('my_recipes/', views.my_recipes, name='my_recipes')
]
