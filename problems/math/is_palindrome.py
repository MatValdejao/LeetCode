"""

LeetCode - isPalindrome

Time: O(?)
Space: O(?)

"""

import pytest

class Solution: 
    def isPalindrome(self, x: int, Debug=False) -> bool:
        if str(x) == '':
           raise ValueError('Input must be a integer')
        
        if len(str(x)) == 1:
            return True



# create debug call
if __name__ == '__main__':
    Solution().isPalindrome(121, Debug=True) == True