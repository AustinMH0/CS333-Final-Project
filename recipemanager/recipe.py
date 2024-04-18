from recipemanager.ingredient import Ingredient


class Recipe:
    def __init__(self, name, prep_time, cook_time, servings):
        self.ingredients = []
        self.name = name
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings

    def add_ingredient(self, ingredients: Ingredient):
        self.ingredients.append(ingredients)

    def remove_ingredient(self, ingredients: Ingredient):
        self.ingredients.remove(ingredients)
