from recipemanager.recipe import Recipe


class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe: Recipe):
        self.recipes.remove(recipe)

    def get_recipes_by_time(self, requested_time):
        for recipe in self.recipes:
            total_time = recipe.prep_time + recipe.cook_time
            if total_time <= requested_time:
                return recipe

    def get_recipes_by_ingredients(self, ingredient_label):
        for recipe in self.recipes:
            if ingredient_label in recipe.ingredients:
                return recipe

    def sort_recipes_by_time(self):
        for recipe in self.recipes:
            total_time = recipe.prep_time + recipe.cook_time
            sorted(recipe, key=lambda recipe_time: total_time)

    def sort_recipes_by_ingredients(self):
        for recipe in self.recipes:
            sorted(recipe, key=lambda ingredients: recipe.ingredients)

