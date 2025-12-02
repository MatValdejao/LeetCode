# Problem Statement (Zigzag Conversion Problem)
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);

## Constraints (from LeetCode)
- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'.
- 1 <= numRows <= 1000

## Execution
1. First step is to deal with edge cases (__len(string) <= 1__ and __numRows == 1__)
2. Initalize lists to store each character
3. Index through string and use direction (1 or -1) variable to move through rows
4. When index reaches numRows - 1, change direction to zigzag
5. Add characters to lists, join all lists together

## Complexity
Time Complexity: O(n) linear complexity (where n is len(s)), looping thrugh each character once
Space Complexity: O(n) linear complexity, characters stored in n lists

Complexity for this problem optimized to linear.

## Usage
- Run git clone to copy repo
- Setup up venv 
- Install dependencies (run pip install -r requirements.txt)
- Run tests via pytest (can use -v for verbose)
- Debug if required -> python3 cwd/problems/strings/zigzag_conversion.py
    - Purpose of debug flag with \_\_main\_\_