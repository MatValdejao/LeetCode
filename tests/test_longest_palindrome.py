"""

Test file for Longest Palindromic Sequence

"""

from problems.strings.longest_palindrome import Solution

# pytest to raise errors
import pytest

# import re to test whether input has allowed characters
import re


"""
Normal Cases
"""

def test_example_1():
    # leetcode base case
    assert Solution().longestPalindrome('babad') == ('bab' or 'aba')

def test_example_2():
    # leetcode base case
    assert Solution().longestPalindrome('cbbd') == 'bb'

def test_example_3():
    # my own base case
    assert Solution().longestPalidrome('forgeeksskeegfor') == 'geeksskeeg'
 
def test_example_4():
    # one more base case
    assert Solution().longestPalindrome('racecar') == 'racecar'


"""
Some edge cases (string cannot be empty, will raise error)
"""

def test_no_palindrome():
    # string with no palindrome
    assert Solution().longestPalindrome('abc') == 'a' # no a palindrome so first letter returned

def test_empty_string():
    # empty string input
    with pytest.raises(ValueError):
        Solution().longestPalindrome('')

def test_improper_character():
    # character error
    with pytest.raises(ValueError):
        Solution().longestPalindrome('assa*')

def test_case_sensitive():
    # case to be treated as different letters
    assert Solution().longestPalindrome('Aa') == ('A' or 'a')