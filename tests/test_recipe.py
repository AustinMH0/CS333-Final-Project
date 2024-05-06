import unittest
from recipemanager.recipe import Recipe
from recipemanager.ingredient import Ingredient


class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.grilled_cheese = Recipe('Grilled Cheese', 5, 5, 1)

        self.gc_ingredients = {Ingredient('Bread', '1 slice'),
                               Ingredient('Mozzarella Cheese', '2 oz'),
                               Ingredient('Tomato', '2 slices'),
                               Ingredient('Basil', '1 oz')}

        self.grilled_cheese.add_multiple_ingredients(self.gc_ingredients)
        self.new_ingredient = Ingredient('Cream Cheese', '4 oz')
        # self.grilled_cheese.print_ingredients()

    def test_add_multiple_ingredients(self):
        self.assertEqual(4, self.grilled_cheese.ingredient_size())

    def test_add_ingredient(self):
        self.grilled_cheese.add_ingredient(self.new_ingredient)
        self.assertEqual(5, self.grilled_cheese.ingredient_size())

    def test_remove_ingredient(self):
        self.grilled_cheese.add_ingredient(self.new_ingredient)
        # self.grilled_cheese.print_ingredients()
        self.a_ingredient = Ingredient('meat', '1')
        self.grilled_cheese.add_ingredient(self.a_ingredient)
        remove = self.grilled_cheese.get_ingredient_by_label('meat')
        self.grilled_cheese.remove_ingredient(remove)
        # print('\n')
        # self.grilled_cheese.print_ingredients()
        self.assertEqual(5, self.grilled_cheese.ingredient_size())

    def test_remove_all_ingredients(self):
        self.grilled_cheese.remove_all_ingredients()
        self.assertEqual(0, self.grilled_cheese.ingredient_size())

    def test_is_ingredient_in_recipe(self):
        self.assertTrue(self.grilled_cheese.is_ingredient('Bread'))

    def test_label_amount(self):
        # print('Basil : ' + self.grilled_cheese.get_label_amount('Basil'))
        self.assertEqual('1 oz', self.grilled_cheese.get_label_amount('Basil'))

    def test_amount_of_ingredient(self):
        # print('2 slices of: ' + self.grilled_cheese.get_amount_of_ingredient('2 slices'))
        self.assertEqual('Tomato', self.grilled_cheese.get_amount_of_ingredient('2 slices'))


if __name__ == '__main__':
    unittest.main()
