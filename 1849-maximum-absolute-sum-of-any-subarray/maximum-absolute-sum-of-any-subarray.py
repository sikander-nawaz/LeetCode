class Solution:
    def maxAbsoluteSum(self, nums):
        n = len(nums)
        max_ending_here = nums[0]
        min_ending_here = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]
        
        for i in range(1, n):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            min_ending_here = min(nums[i], min_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)
            min_so_far = min(min_so_far, min_ending_here)
        
        return max(abs(max_so_far), abs(min_so_far))