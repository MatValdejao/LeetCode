"""

LeetCode - Find Median Sorted Array 

Time: O(?)
Space: O(?)

"""

from typing import List 

class Solution():
    def find_median_sorted_array(self, nums1: List[int], nums2: List[int], debug=False) -> float:
        # first step is tp combine and sort both lists
        new_list = nums1 + nums2
        new_list.sort()

        if debug:
            print(new_list)


if __name__ == '__main__':
    Solution().find_median_sorted_array([1, 2], [3, 4], debug=True) == 2.5
