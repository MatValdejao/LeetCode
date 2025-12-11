"""

Test file for Merdian Sorted Array Problem

"""

from problems.array.median_sorted_array import Solution

import pytest


"""

Normal Cases

"""

# first base leetcode test
def test_base_1():
    assert Solution().find_median_sorted_array([1, 3], [2]) == 2

# second base leetcode test
def test_base_2():
    assert Solution().find_median_sorted_array([1, 2], [3, 4]) == 2.5

# adding a thirg base case
def test_base_3():
    assert Solution().find_median_sorted_array([1, 1], [1, 1]) == 1

# adding a mixed number base case
def test_base_4():
    assert Solution().find_median_sorted_array([-3, 4, 2, -3, 5], [1, -1, 4, 3]) == 2

"""

Edge Cases

"""

# one edge case is one list is empty
def test_one_empty():
    assert Solution().find_median_sorted_array([], [1]) == 1

# both lists are empty
def test_both_empty():
    # will make equal to zero, still return float but idea of nothingness
    assert Solution().find_median_sorted_array([], []) == 0 

# another one empty, but with second larger list
def test_one_empty_larger():
    assert Solution().find_median_sorted_array([], [1, 2, 3, 4]) == 2.5

# will insert arrays of different sized in edge case
def test_different_sizes():
    assert Solution().find_median_sorted_array([1, 2], [3, 4, 5, 6, 7, 8, 9]) == 5

# all negative numbers, will add a mixed one to base cases
def test_all_neg():
    assert Solution().find_median_sorted_array([-5, -3, -1], [-2, -1]) == -2

# adding stress test from now
def test_stress():
    assert Solution().find_median_sorted_array(list(range(0, 1001, 1)), list(range(0, 1000, 1))) == 500