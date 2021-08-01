import unittest

from dynamic_programming.knapsack import Item, knapsack01


class KnapsackTestCase(unittest.TestCase):

    def test_knapsack01(self):
        items = [Item(2, 1), Item(3, 2), Item(4, 5), Item(5, 6)]
        picked_items, profit = knapsack01(items, 8)

        self.assertEqual(8, profit)
        self.assertListEqual([Item(5, 6), Item(3, 2)], picked_items)

    def test_knapsack01_2(self):
        items = [Item(1, 1), Item(3, 4), Item(4, 5), Item(5, 7)]
        picked_items, profit = knapsack01(items, 7)

        self.assertEqual(9, profit)
        self.assertListEqual([Item(4, 5), Item(3, 4)], picked_items)


if __name__ == '__main__':
    unittest.main()
