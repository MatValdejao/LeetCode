"""
Test file for is palindrome problem
"""

from problems.math.is_palindrome import Solution, SolutionNoConversion
import pytest 


"""
Normal Cases
"""

# Leetcode first base case
def test_example_1():
    Solution().isPalindrome(121) == True
    SolutionNoConversion().isPalindrome(121) == True

# Leetcode second base case
def test_example_2():
    Solution().isPalindrome(-121) == False
    SolutionNoConversion().isPalindrome(-121) == False

# Leetcode thrid base case
def test_example_3():
    Solution().isPalindrome(10) == False
    SolutionNoConversion().isPalindrome(10) == False

# extra base case
def test_example_4():
    Solution().isPalindrome(1010101) == True
    SolutionNoConversion().isPalindrome(1010101) == True


"""
Edge Case
"""

# edge case when input is single digit
def test_single_digit():
    Solution().isPalindrome(8) == True
    SolutionNoConversion().isPalindrome(8) == True

# negative single digit
def test_neg_single():
    Solution().isPalindrome(-8) == False
    SolutionNoConversion().isPalindrome(-8) == False

# will also raise error when empty input provided
def test_blank():
    with pytest.raises(ValueError):
        Solution().isPalindrome(None)
    with pytest.raises(ValueError):
        SolutionNoConversion().isPalindrome(None)