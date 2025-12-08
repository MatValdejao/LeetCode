"""

LeetCode - isPalindrome

Time: O(n) -> x has n digits, reverse variable is of same digit length as x
Space: O(n) -> reverse stores string of same length n as converted x

"""

import pytest

class Solution: 
    def isPalindrome(self, x: int, Debug=False) -> bool:
        if x == None:
           raise ValueError('Input must be a integer')

        reverse = str(x)[::-1]
        return reverse == str(x)
            

# create debug call
if __name__ == '__main__':
    Solution().isPalindrome(12, Debug=True) == True