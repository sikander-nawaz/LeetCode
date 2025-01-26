class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack: list[int] = []
        for idx in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[idx]:
                stack.append(idx)
        max_length: int = 0
        for right in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[right]:
                max_length = max(max_length, right - stack.pop())
        return max_length