# Problem Statement (Is Palindrome Problem)
Given an integer **x**, return true if **x** is a palindrome, and false otherwise.

Follow-up: Can the problem be solved without converting to string first. 

# Constraints
- -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1 

# Execution
## Two Solutions Coded
### Solution 1: With String Conversion
1. No input edge case raises value error
2. Convert x to string and reverse with splicing
3. Compare to original string, returning boolean

### Solution 2: No String Conversion
1. No input edge case raises value error
2. If number is negative, return false (i.e. -121 != 121- )
3. Initialize reverse at 0 and x placeholder for loop; (number = x)
4. Find reverse by finding remainder of number variable when divided by ten, added to reverse multiplied by 10 
5. Update number variable by dividing by 10 and rounding down
6. Loop process until x is 0

- Example: 
    - reverse = 0, number = x = 121
    - First loop iteration:
        - reverse = 0 * 10 + 121 % 10 = 1
        - number = 121 // 10 = 12
    - Second loop iteration (number = 12):
        - reverse = 1 * 10 + 12 % 10 = 12
        - number = 12 // 10 = 1
    - Third loop iteration (number = 1):
        - reverse = 12 * 10 + 1 % 10 = 121
        - number = 1 // 10 = 0
    - Fourth loop won't run as number == 0.


# Complexity
## With Conversion:
- Time: O(n) -> splices backwards through string of length n
- Space: O(n) -> stores reverse string of length n

## Without Conversion:
- Time: O(n) -> n loops for n digits in x
- Space: O(1) -> reverse is stored in one variable

# Debugging
- Debug if required with -> python3 cwd/problems/strings/is_palindrome.py
    - Purpose of debug flag with \_\_main\_\_