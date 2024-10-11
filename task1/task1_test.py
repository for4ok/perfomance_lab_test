import unittest

from task1 import formula


class TestMathFunctions(unittest.TestCase):
    def test_formula(self):
        self.assertEqual(formula(5, 4), '14253')
        self.assertEqual(formula(12, 10), '11074')
        self.assertEqual(formula(25, 32), '17131925612182451117234101622391521281420')


if __name__ == '__main__':
    unittest.main()
