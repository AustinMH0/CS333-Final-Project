from recipemanager.recipe import Recipe


class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe: Recipe):
        self.recipes.remove(recipe)

    def get_recipe_by_name(self, name):
        for recipe in self.recipes:
            if name in recipe.name:
                return recipe

    def get_recipes_by_time(self, requested_time):
        recipes_by_time = [recipe for recipe in self.recipes if
                           recipe.total_time <= requested_time]

        return recipes_by_time
        # for recipe in recipes_by_time:
        #     return recipe.name

    def get_recipes_by_ingredients(self, ingredient_label):
        recipes_by_ingredients = [recipe for recipe in self.recipes if
                                  recipe.is_ingredient(ingredient_label)]

        return recipes_by_ingredients

    def sort_recipes_by_time(self):
        return sorted(self.recipes, key=lambda recipe: recipe.total_time)

    def get_recipe_book_size(self):
        return len(self.recipes)

    def __str__(self):
        recipes = str(self.recipes)[1:-1]
        recipes = recipes.replace(', ', '\n')
        return recipes

    def __repr__(self):
        return f'Recipes: {self.recipes}'
