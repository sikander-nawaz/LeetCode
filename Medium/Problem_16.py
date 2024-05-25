# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# SOLUTION:

class Solution:
    def search(self, x: List[int], target: int) -> int:
        n = len(x)
        
        def findK():
            if n == 1:
                return 0
            if n==2:
                if x[0]<x[1]: return 1
                else: return 0
            l=0
            r=n
            while l < r:
                m = (r + l) // 2
                if m==n-1 or x[m]>x[m+1]: return m
                if x[m]>x[l]: l=m
                else: r=m
            return m
        
        k=findK()
        
        if target >= x[0]:
            i = bisect_left(x, target, hi=k)
            if i<n and x[i] == target:
                return i
            return -1
        else:
            i = bisect_left(x, target, lo=k+1)
            if i<n and x[i] == target:
                return i
            return -1