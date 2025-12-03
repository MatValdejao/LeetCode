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


if __name__ == '__main__':
    Solution().longestPalindrome('racecar', Debug=True) == 'racecar'