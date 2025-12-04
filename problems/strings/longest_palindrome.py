"""

Time: O(?)
Space: O(?)

"""

class Solution: 
    def longestPalindrome(self, s: str, Debug=False) -> str:
        # test invalid inputs
        if len(s) == 0: raise ValueError('Input string must not be empty')

        if not s.isalnum():
            raise ValueError('Input must contain only letters and digit')

        # will attempt a two pointer solution from center
        def center_base(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # return left inbounds from -1
            return s[left+1:right]
        
        # initialize palindrome string as first letter of s
        res = s[0]

        # loop through input string, difference between odd count and even
        for i in range(len(s) - 1):
            # if odd start from same letter on center_base function
            odd = center_base(i, i)
            # offset start for even
            even = center_base(i , i + 1)
            
            # now to check all palindromes found for largest
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even

        return res

if __name__ == '__main__':
    Solution().longestPalindrome('racecar', Debug=True) == 'racecar'