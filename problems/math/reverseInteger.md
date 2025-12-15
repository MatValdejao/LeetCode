# Problem Statement (Is Palindrome Problem)
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2<sup>31</sup>, 2<sup>31</sup> - 1], then return error.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

# Constraints
- -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

# Execution
1. Check both no input situation and larger than 32-bit situation
2. Local variable to register whether x is negative or not
3. Take aboslute value of x
4. Reverse by simple string comversion
5. Check whether reverse x overflow 32-bit limit
    - If so, return 0
6. Revert reverse back to integer and add negative number by referring to local negative boolean value

# Complexity
Time Complexity: O(n) for time for reversal of string of length n
Space Complexity: O(n) for space for storage of reverse string of length n

# Debugging
- Debug if required with -> python3 cwd/problems/strings/reverse_integer.py
    - Purpose of debug flag with \_\_main\_\_

