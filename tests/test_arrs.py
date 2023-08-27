import unittest
from utils import arrs, dicts


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], -1, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 0), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], - 3, 4), [2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3], -4), [1, 2, 3])

    def test_get_val(self):
        self.assertEqual(dicts.get_val({"pk": 1}, "pk"), 1)
        self.assertEqual(dicts.get_val({"pk": 1}, "pk", "git"), 1)
        self.assertEqual(dicts.get_val({}, "pk", "git"), "git")
        self.assertEqual(dicts.get_val({}, "pk", "bazaar"), "bazaar")

