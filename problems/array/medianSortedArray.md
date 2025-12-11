# Problem Statement (Is Palindrome Problem)
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)). 

# Constraints
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -106 <= nums1[i], nums2[i] <= 106

# Execution
1. Combine both lists and sort
2. Initialize median variable
3. If both lists are empty, retun 0 with if statement
4. Check if length of combined list is odd or even
5. If length is odd, return value of middle index, if not, take average of two middle indexes and return value

# Complexity

Time: O(m+nlog(m+n)) -> most of the time complexity comes from sorting the lists. log(m+n) levels on sort, m+n sorts
Space: O(m+n) -> storage of combined sorted new list

# Debugging
- Debug if required with -> python3 cwd/problems/array/median_sorted_array.py
    - Purpose of debug flag with \_\_main\_\_
