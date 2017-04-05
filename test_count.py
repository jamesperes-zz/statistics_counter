import unittest
from script import count


class CountTest(unittest.TestCase):

    def test_number_is_int_(self):
        self.assertTrue(int(2), count(2))
        self.assertFalse(count('2'))


if __name__ == '__main__':
    unittest.main()
