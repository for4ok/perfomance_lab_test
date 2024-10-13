import unittest
import os

from task4 import min_moves, read_numbers


class TestMinMoves(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_numbers.txt'
        with open(self.test_file, 'w') as f:
            f.write("1\n10\n2\n9\n")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_numbers(self):
        expected_output = [1, 10, 2, 9]
        actual_output = read_numbers(self.test_file)
        self.assertEqual(actual_output, expected_output)

    def test_min_moves(self):
        nums = [1, 10, 2, 9]
        expected_moves = 16  # Расчет: 1 + 0 + 1 + 8 + 7 = 16
        actual_moves = min_moves(nums)
        self.assertEqual(actual_moves, expected_moves)


if __name__ == '__main__':
    unittest.main()
