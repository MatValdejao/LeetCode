"""

Test file for reverse integer Leetcode problem

"""

from problems.math.reverse_integer import Solution

# raise error for no input
import pytest

"""

Normal Cases

"""

# leetcode first base case
def test_base_1():
    assert Solution.reverse(123) == 321

# second leetcode base case
def test_base_2():
    assert Solution.reverse(-123) == -321

# third leetcode base case
def test_base_3():
    assert Solution.reverse(120) == 21


"""

Edge Cases

"""

# test no input case
def test_no_input():
    with pytest.raises(ValueError):
        Solution.reverse()

