import unittest

from solution_code import *

class TestMethods(unittest.TestCase):

    def test_function(self):

        self.assertEqual(decode("я люблю ананасы"), [5, 5, 12, 4, 11, 12, 4, 5, 10, 14, 10, 14, 10, 18, 1])

        self.assertEqual(decode("сироп"), [18, 9, 14, 17, 15, 16])

        self.assertEqual(decode("лесничий"), [12, 15, 18, 14, 9, 15, 15, 9, 10])

        self.assertEqual(decode("меч"),  [13, 15, 15])

        self.assertEqual(decode("ахиллес"),  [10, 13, 9, 12, 12, 15, 18])

        self.assertEqual(decode("пруд"),  [16, 17, 11, 14])

        self.assertEqual(decode("рефрижератор"),  [17, 15, 12, 17, 9, 16, 15, 17, 10, 10, 15, 17])

if __name__ == '__main__':

    unittest.main()