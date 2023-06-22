#test_fields.py

import unittest
from fields import *
class TestField(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 5
        self.h = 10
    def test_rectangle_with_corrent_value(self):
        result = rectangle(self.a, self.b)
        self.assertEqual(result, 50)

    def test_all_with_incorrect_value(self):
        #self.assertRaises(ValueError, rectangle, True , '*')
        with self.assertRaises(ValueError):
            rectangle(True , "Incorect Value")
            triangle(True , "Incorect Value")
            trapezoid(True , ['incorect', 'value'], "Incorect Value")

    def test_triangle_with_corrent_value(self):
        result = triangle(self.a, self.b)
        self.assertEqual(result, 25)

    def test_trapezoid_with_corrent_value(self):
        result = trapezoid(self.a, self.b, self.h)
        exoected = 75
        self.assertEqual(result, exoected)
    def tearDown(self):
        del self.a
        del self.b
        del self.h

if __name__ == '__main__':
    unittest.main()