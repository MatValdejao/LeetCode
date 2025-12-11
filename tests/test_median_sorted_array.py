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

"""

Edge Cases

"""