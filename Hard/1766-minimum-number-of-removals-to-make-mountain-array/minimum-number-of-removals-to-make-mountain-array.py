class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        # Calculate LIS from the left
        left_lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left_lis[i] = max(left_lis[i], left_lis[j] + 1)

        # Calculate LDS from the right
        right_lis = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    right_lis[i] = max(right_lis[i], right_lis[j] + 1)

        # Calculate the maximum length of mountain array
        max_mountain_length = 0
        for i in range(1, n - 1):
            if left_lis[i] > 1 and right_lis[i] > 1:  # Must be a peak
                max_mountain_length = max(max_mountain_length, left_lis[i] + right_lis[i] - 1)

        # Minimum removals
        return n - max_mountain_length if max_mountain_length > 0 else n