""""

LeetCode: Letter Combinations

Time: O(?)
Space: O(?)

"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # test for empty input
        if digits == '': return []

        # test for 0 or 1, invalidate any string with 0 or 1
        if any(d not in '23456789' for d in digits): 
            raise ValueError('Input must contain only digits between 2-9')

        
