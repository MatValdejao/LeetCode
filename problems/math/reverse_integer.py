"""

LeetCode: Revere String

Time: O(n) -> Reversing the string requires n steps, for n string length of conversion
Space: O(n) -> Storage of two variables, a reverse string of length n stored

"""

import pytest

class Solution:
    def reverse(self, x: int, Debug=False) -> int:
        if x == None: raise ValueError('Must input integer')
        if x < -2**31 or x > 2**31 - 1:
            raise ValueError('Outside bit-32 range')
        
        # check if number is neg and save
        negative = False
        if x < 0:
            negative = True

        # get absolute value
        x = abs(x)

        # convert to string, reverse and return reverse with checked neg
        rev = str(x)[::-1]
        # if Debug:
        #     print(rev)

        # adding check for if return value is to large, add test case
        if int(rev) > 2**31-1: return 0

        # check if number was negative and add back to return 
        if negative: return -(int(rev))
        else: return int(rev)


# inlined debug
if __name__ == '__main__':
    Solution().reverse(-123, Debug=True) == -321 