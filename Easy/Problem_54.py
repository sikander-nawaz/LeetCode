# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
 

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# SOLUTION:

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        R, L = 0, len(nums)-1
        while R <= L:
            MID = R + (L-R)//2
            if nums[MID] == target:
                return MID
            elif  nums[MID] > target:
                L = MID - 1
            else:
                R = MID + 1
            if R > L:
                return R
