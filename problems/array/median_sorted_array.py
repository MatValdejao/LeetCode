"""

LeetCode - Find Median Sorted Array 

Time: O(m+n) -> most of the time complexity comes from sorting the lists 
Space: O(m+n) -> storage of combined sorted new list

"""

from typing import List 

class Solution():
    def find_median_sorted_array(self, nums1: List[int], nums2: List[int], debug=False) -> float:
        # first step is tp combine and sort both lists
        new_list = nums1 + nums2
        new_list.sort()
        # initialize median
        median = 0

        # if debug:
        #     print(new_list)
        if len(new_list) == 0: return 0

        # need to differentiate between odd sized and even for median
        if len(new_list) % 2 == 1:
            # for odd sized, find the middle index
            median = new_list[len(new_list)//2]
        else: 
            # for even sized, take average of center indexes
            median = (new_list[len(new_list)//2-1] + new_list[len(new_list)//2]) / 2

        if debug:
            print(median)
        
        return median
         

if __name__ == '__main__':
    Solution().find_median_sorted_array([1, 2], [3, 4], debug=True) == 2.5
    Solution().find_median_sorted_array([1, 2], [3, 4, 5], debug=True) == 3
