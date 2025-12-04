# Problem Statement (Longest Palindromic Substring)
Given a string s, return the longest palindromic substring in s.

## Constraints
- 1 <= s.length <= 1000 (where s is input string)
- **s** consists of only digits and English letters

## Execution
1. First step is to deal with edge cases where string length is zero or any non-alphanumeric are used
2. Defining center_base function, that expands input string from center, checking whether right and left indices match
3. Initialize base palindrome as first letter
4. Loop through characters in s, defining an even and an odd letter count palindrome
5. Check if newly formed palindrome larger than based length one palindrome defined earlier
6. Return max length palindrome

## Complexity
Time Complexity: O(n^2) where n is length of input string. 2n-1 possible centers (from even and odd possibilities) and for loop iterating through n characters.
Space Complexity: O(n), storage for left and right indices of s

## Usage and Debug
- Debug if required with -> python3 cwd/problems/strings/longestPalindrome.py
    - Purpose of debug flag with \_\_main\_\_
