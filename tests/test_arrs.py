import pytest
from utils import arrs, dicts


def test_get(fixture_get_list):
    assert arrs.get(fixture_get_list, 0) == 1
    assert arrs.get(fixture_get_list, 1) == 2
    assert arrs.get(fixture_get_list, 2) == 3
    assert arrs.get(fixture_get_list, 1, "test") == 2
    assert arrs.get(fixture_get_list, -1, default=0) == 0


def test_my_slice(fixture_my_slice, fixture_my_slice_none):
    assert arrs.my_slice(fixture_my_slice, 1, 3) == [2, 3]
    assert arrs.my_slice(fixture_my_slice, 1) == [2, 3, 4]
    assert arrs.my_slice(fixture_my_slice_none, 0) == []
    assert arrs.my_slice(fixture_my_slice, - 3, 4) == [2, 3, 4]
    assert arrs.my_slice(fixture_my_slice, - 5) == [1, 2, 3, 4]


def test_get_val(fixture_get_val, fixture_get_val_def):
    assert dicts.get_val(fixture_get_val, "pk") == 1
    assert dicts.get_val(fixture_get_val, "pk", "git") == 1
    assert dicts.get_val(fixture_get_val_def, "pk", "git") == "git"




















# class TestArrs(unittest.TestCase):
#
#     def test_get(self):
#         self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
#         self.assertEqual(arrs.get([], -1, "test"), "test")
#
#     def test_slice(self):
#         self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
#         self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
#         self.assertEqual(arrs.my_slice([], 0), [])
#         self.assertEqual(arrs.my_slice([1, 2, 3, 4], - 3, 4), [2, 3, 4])
#         self.assertEqual(arrs.my_slice([1, 2, 3], -4), [1, 2, 3])
#
#     def test_get_val(self):
#         self.assertEqual(dicts.get_val({"pk": 1}, "pk"), 1)
#         self.assertEqual(dicts.get_val({"pk": 1}, "pk", "git"), 1)
#         self.assertEqual(dicts.get_val({}, "pk", "git"), "git")
#         self.assertEqual(dicts.get_val({}, "pk", "bazaar"), "bazaar")

