import unittest
from recipemanager.ingredient import Ingredient
from recipemanager.recipe import Recipe
from recipemanager.recipe_book import RecipeBook


class TestRecipeBook(unittest.TestCase):
    def setUp(self):
        self.grilled_cheese = Recipe('Grilled Cheese', 5, 5, 1)

        self.gc_ingredients = {Ingredient('Bread', '1 slice'),
                               Ingredient('Mozzarella Cheese', '2 oz'),
                               Ingredient('Tomato', '2 slices'),
                               Ingredient('Basil', '1 oz')}

        self.soup = Recipe('Soup', 7, 10, 2)
        self.steak = Recipe('Steak', 20, 60, 4)

        self.soup_ingredient = Ingredient('Tomato', '4')

        self.steak_ingredients = {Ingredient('Tri-tip', '1 pound'),
                                  Ingredient('Seasoning', '2 oz'),
                                  Ingredient('Mushrooms', '8 oz'),
                                  Ingredient('Asparagus', '4 oz')}

        self.grilled_cheese.add_multiple_ingredients(self.gc_ingredients)

        self.recipe_book = RecipeBook()
        self.recipe_book.add_recipe(self.grilled_cheese)

    def test_add_recipe(self):
        self.assertEqual(1, self.recipe_book.get_recipe_book_size())
        self.recipe_book.add_recipe(self.soup)
        self.assertEqual(2, self.recipe_book.get_recipe_book_size())

    def test_remove_recipe(self):
        self.recipe_book.remove_recipe(self.grilled_cheese)
        self.assertEqual(0, self.recipe_book.get_recipe_book_size())

    def test_get_recipe_by_name(self):
        self.assertEqual(self.grilled_cheese, self.recipe_book.get_recipe_by_name('Grilled Cheese'))
        self.recipe_book.add_recipe(self.soup)
        self.assertEqual(self.soup, self.recipe_book.get_recipe_by_name('Soup'))

    def test_get_recipes_by_time(self):
        recipes_under_15 = self.recipe_book.get_recipes_by_time(15)
        self.assertEqual(1, len(recipes_under_15))

        self.recipe_book.add_recipe(self.soup)
        recipes_under_20 = self.recipe_book.get_recipes_by_time(20)
        self.assertEqual(2, len(recipes_under_20))

        self.recipe_book.add_recipe(self.steak)
        recipes_under_90 = self.recipe_book.get_recipes_by_time(90)
        self.assertEqual(3, len(recipes_under_90))

    def test_get_recipes_by_ingredients(self):
        self.assertEqual(1, len(self.recipe_book.get_recipes_by_ingredients('Bread')))

        self.soup.add_ingredient(self.soup_ingredient)
        self.recipe_book.add_recipe(self.soup)
        self.assertEqual(2, len(self.recipe_book.get_recipes_by_ingredients('Tomato')))

    def test_sort_recipes_by_time(self):
        self.recipe_book.remove_recipe(self.grilled_cheese)
        self.recipe_book.add_recipe(self.soup)
        self.recipe_book.add_recipe(self.steak)
        self.recipe_book.add_recipe(self.grilled_cheese)
        self.assertTrue(self.recipe_book.sort_recipes_by_time())


if __name__ == '__main__':
    unittest.main()
