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

        # string loop and zigzag
        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == (numRows - 1):
                d = -1 
            # update idx via direction
            idx += d
        if debug:
            print(''.join([char for row in range(numRows) for char in rows[row]]))

        return ''.join([char for row in range(numRows) for char in rows[row]])


# main to be used for local debugging
if __name__ == "__main__":
    # run inline with debug option
    Solution().zigzagConvert("PAYPALISHIRING", 3, debug=True) == "PAHNAPLSIIGYIR"
