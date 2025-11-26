"""
LeetCode: ZigZag Conversion 

Time: O(?)
Space: O(?)

"""

class Solution:
    def zigzagConvert(self, s: str, numRows: int, debug=False) -> str:
        # treat edge cases 
        if len(s) <= 1 or numRows == 1:
            return s
        
        # neew both a row indexer and direction, use list to reorg
        idx, d = 0, 1
        rows = [[] for i in range(numRows)]

        # string loop

        return


if __name__ == "__main__":
    # run inline with debug option
    Solution().convert("PAYPALISHIRING", 3, debug=True) == "PAHNAPLSIIGYIR"
