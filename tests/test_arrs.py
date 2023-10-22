import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3, 4, 5], 2), 3)
        self.assertEqual(arrs.get([1, 2, 3, 4, 5], 10, default="Not found"),"Not found")
        self.assertNotEqual(arrs.get([1, 2, 3, 4, 5], 3), 5)
        self.assertEqual(arrs.get([1, 2, 3, 4, 5], -1), 5)
        self.assertEqual(arrs.get([], 0, default="Empty"), "Empty")
        self.assertEqual(arrs.get([1, 2, 3, 4, 5], 3), int("4"))

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertNotEqual(arrs.my_slice([1, 2, 3, 4, 5]), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 2), [3, 4, 5])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], end=3), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], start=-3, end=-1), [3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], start=2), [3, 4, 5])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], end=2), [1, 2])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], start=-3, end=-2), [3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], start=-5, end=5), [1, 2, 3, 4, 5])
        self.assertEqual(arrs.my_slice([]), [])
        self.assertNotEqual(arrs.my_slice([1, 2, 3, 4, 5]), [])