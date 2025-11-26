""""
Test File for ZigZag Conversion problem.
"""

from strings.zigzag_conversion import Solution

""""
Normal Cases
"""

def test_example_1():
    # leetcode base case
    assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

def test_example_2():
    # another leetcode base case
    assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

def test_example_3():
    # one of my own
    assert Solution().convert("ABCDEFGHIJKLMN", 4) == "AGMBFHLNCEIKDJ"

"""
Some edge cases (empty string, only two rows, rows to num of letter relationship)
"""

def same_letter_count_rows():
    # same number of letters as rows
    assert Solution().convert("Orange", 6) == "Orange"

def one_row():
    # one row
    assert Solution().convert("Orange", 1) == "Orange"

def more_rows_than_letters():
    # more rows
    assert Solution().convert("Orange", 8) == "Orange"

def empty_string():
    # empty input string
    assert Solution().convert("", 4) == ""

