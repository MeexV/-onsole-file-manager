import pytest
import math

def test_filter():
    nums = [1,2,3,4,5,6,7,8,9]
    filter_nums = list(filter(lambda x: x > 5, nums))
    assert filter_nums == [6,7,8,9]

def test_map():
    nums = [1,2,3,4,5,6,7,8,9]
    map_nums = list(map(lambda x: x*11, nums))
    assert map_nums == [11,22,33,44,55,66,77,88,99]

def test_sorted():
    nums = [3, 1, 4, 5, 9, 2, 6, 8]
    sorted_nums = sorted(nums)
    assert sorted_nums == [1, 2, 3, 4, 5, 6, 8, 9]

def test_sqrt():
    assert math.sqrt(36) == 6
    assert math.sqrt(1) == 1

def test_pow():
    assert math.pow(3, 3) == 27

def test_hypot():
    assert math.hypot(3, 4) == 5

