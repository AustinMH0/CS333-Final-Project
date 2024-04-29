import unittest
from recipemanager.ingredient import Ingredient


class TestIngredient(unittest.TestCase):
    def setUp(self):
        self.ingredient = Ingredient('Cheese', '3 oz')

    def test_ingredient_attributes(self):
        self.assertEqual(self.ingredient.label, 'Cheese')
        self.assertEqual(self.ingredient.amount, '3 oz')


if __name__ == '__main__':
    unittest.main()
