""""
Test File for ZigZag Conversion problem.
"""

from problems.strings.zigzag_conversion import Solution

""""
Normal Cases
"""

def test_example_1():
    # leetcode base case
    assert Solution().zigzagConvert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

def test_example_2():
    # another leetcode base case
    assert Solution().zigzagConvert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

def test_example_3():
    # one of my own
    assert Solution().zigzagConvert("ABCDEFGHIJKLMN", 4) == "AGMBFHLNCEIKDJ"

"""
Some edge cases (empty string, only two rows, rows to num of letter relationship)
"""

def test_same_letter_count_rows():
    # same number of letters as rows
    assert Solution().zigzagConvert("Orange", 6) == "Orange"

def test_one_row():
    # one row
    assert Solution().zigzagConvert("Orange", 1) == "Orange"

def test_more_rows_than_letters():
    # more rows
    assert Solution().zigzagConvert("Orange", 8) == "Orange"

def test_empty_string():
    # empty input string
    assert Solution().zigzagConvert("", 4) == ""

