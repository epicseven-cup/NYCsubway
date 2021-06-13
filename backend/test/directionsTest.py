import unittest

from backend.directions import readingCSV


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
        readingCSV("filename.csv")


if __name__ == '__main__':
    unittest.main()
