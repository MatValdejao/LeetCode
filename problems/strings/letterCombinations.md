# Problem Statement (Zigzag Conversion Problem)
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 0 or 1 are invalid inputs.

![Telephone Digits Example](assets/leetCodeDigits.png)

## Constraints
- digits.length <= 4 
- digits d has range('2', '9)

## Execution
1. Deal with empty string and 0 or 1 inputs
2. Define a backtrack function that goes through each digit in digits, and calls iself to next digit
3. Map each recusrion call to letters in letter dictionary
4. Append each combination when recursion call excedes digits length
5. Return res 

## Complexity

Time Complexity: O(4^n*n) -> Each digit can map to a max 4 letters, so 4ˆn for all combinations. Backtrack explores all paths in letter dict.

Space Complexity: O(4^n*n) -> Total space is all combinations.

## Usage and Debug
- Debug if required with -> python3 cwd/problems/strings/zigzag_conversion.py
    - Purpose of debug flag with \_\_main\_\_