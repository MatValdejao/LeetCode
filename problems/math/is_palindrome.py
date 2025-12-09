"""

LeetCode - isPalindrome

Time: O(n) -> x has n digits, reverse variable is of same digit length as x
Space: O(n) -> reverse stores string of same length n as converted x

"""

import pytest

class Solution: 
    def isPalindrome(self, x: int, Debug=False) -> bool:
        # check no input 
        if x == None:
           raise ValueError('Must input a number.')

        # reverse with string conversion and compare
        reverse = str(x)[::-1]
        return reverse == str(x)
    
class SolutionNoConversion:
    def isPalindrome(self, x: int, Debug=False) -> bool:
        # check for negative numbers
        if x < 0: return False

        # check for no input
        if x == None:
            raise ValueError('Must input an number.')
        
        reverse = 0

        # us remainder to get last integer
        while x != 0:
            # remainder of input, multiplying by ten to build inverse
            reverse = reverse * 10 + x % 10
            # print(reverse)
            
            # update x
            x = x // 10
            
        return reverse == 
            
            

            

# create debug call
if __name__ == '__main__':
    Solution().isPalindrome(12321, Debug=True) == False
    SolutionNoConversion().isPalindrome(12321, Debug=True) == False