"""

Time: O(?)
Space: O(?)

"""

import re

class Solution: 
    def longestPalindrome(self, s: str) -> str:
        # test invalid inputs
        if len(s) == 0: raise ValueError('Input string must not be empty')

        if not s.isalnum():
            raise ValueError('Input must contain only letters and digit')


        # will attempt a two pointer solution from center

       