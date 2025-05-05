class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsSet = set(nums)
        for i in numsSet:
            if (i - 1) not in numsSet:
                count = 1
                while (i + count) in numsSet:
                    count += 1
                longest = max(longest, count)
        return longest