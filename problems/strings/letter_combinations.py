""""

LeetCode: Letter Combinations

Time: O(4^n * n) -> learing step, forgot to add (* n) for all digits, checked in leetcode
Space: O(n) -> list of digit combinations

"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str, debug=False) -> List[str]:
        # test for empty input
        if digits == '': return []

        # test for 0 or 1, invalidate any string with 0 or 1
        if any(d not in '23456789' for d in digits): 
            raise ValueError('Input must contain only digits between 2-9')

        # map digits
        digits_map_phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        # create a bakctrack function for digits
        def backtrack(idx, combinations):
            if idx == len(digits):
                res.append(combinations[:])
                return res
            
            # look at digit dictionary and loop through letters, add to combination
            for letter in digits_map_phone[digits[idx]]:
                backtrack(idx+1, combinations + letter)
                
        # call backtrack
        backtrack(0, '')

        if debug:
            print(res)

        return res

if __name__ == '__main__':
    # set up debug
    Solution().letterCombinations('22', debug=True) == ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']