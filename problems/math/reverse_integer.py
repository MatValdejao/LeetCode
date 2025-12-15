"""

LeetCode: Revere String

Time: O(?) ->
Space: O(?) ->

"""

import pytest

class Solution:
    def reverse(self, x: int, Debug=False) -> int:
        if x == None: raise ValueError('Must input integer')
        if x >= 2**31 - 1:
            raise ValueError('Outside bit-32 range')
        
        # check if number is neg and save
        negative = False
        if x < 0:
            negative = True

        # get absolute value
        x = abs(x)

        # convert to string, reverse and return reverse with checked neg
        rev = str(x)[::-1]
        if Debug:
            print(rev)
        
        # check if number was negative and add back to return 
        if negative: return -(int(rev))
        else: return int(rev)


# inlined debug
if __name__ == '__main__':
    Solution().reverse(-123, Debug=True) == -321 