# Bade bhai, Python me kaafi short and sweet hota hai. 
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        res, i = 0, 0
        while i < len(nums):
            j = i
            while i < len(nums) and nums[i] == max_num:
                i += 1
            res = max(res, i - j)
            i = j + 1 if j == i else i
        return res