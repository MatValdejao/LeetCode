""""
Test file for Letter Combintations
"""

from problems.strings.letter_combinations import Solution


""""
Normal Cases
"""

def test_example_1():
    # leetcode base case
    assert Solution().letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf','ce', 'ce', 'cf']

def test_example_2():
    # leetcode base case
    assert Solution().letterCombinations('2') == ['a', 'b', 'c']

def test_example_3():
    # my own base case
    assert Solution().letterCombinations('45') == ['gj', 'gk', 'gl', 'hj', 'hk', 'hl', 'ij', 'ik', 'il']

def test_largest_input():
    # leetcode adds len(string) <= 4 constraint, test this
    assert Solution().letterCombinations('2345') == [
    "adgj", "adgk", "adgl",
    "adhj", "adhk", "adhl",
    "adij", "adik", "adil",

    "aegj", "aegk", "aegl",
    "aehj", "aehk", "aehl",
    "aeij", "aeik", "aeil",

    "afgj", "afgk", "afgl",
    "afhj", "afhk", "afhl",
    "afij", "afik", "afil",

    "bdgj", "bdgk", "bdgl",
    "bdhj", "bdhk", "bdhl",
    "bdij", "bdik", "bdil",

    "begj", "begk", "begl",
    "behj", "behk", "behl",
    "beij", "beik", "beil",

    "bfgj", "bfgk", "bfgl",
    "bfhj", "bfhk", "bfhl",
    "bfij", "bfik", "bfil",

    "cdgj", "cdgk", "cdgl",
    "cdhj", "cdhk", "cdhl",
    "cdij", "cdik", "cdil",

    "cegj", "cegk", "cegl",
    "cehj", "cehk", "cehl",
    "ceij", "ceik", "ceil",

    "cfgj", "cfgk", "cfgl",
    "cfhj", "cfhk", "cfhl",
    "cfij", "cfik", "cfil",
    ]

""""
Some edge cases 
"""

def test_empty_input():
    # empty string input (even though there is a len > 1 constraint as well)
    assert Solution().letterCombinations('') == []

def test_repeat_num():
    # same digit input
    assert Solution().letterCombinations('22') == ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
