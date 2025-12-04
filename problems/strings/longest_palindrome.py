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

        def center_base(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
        # will attempt a two pointer solution from center


if __name__ == '__main__':
    Solution().longestPalindrome('racecar', Debug=True) == 'racecar'