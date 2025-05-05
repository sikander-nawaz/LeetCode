class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        count_ones = sum(nums)
  
        if count_ones == 0 or count_ones == n:
            return 0

        nums_extended = nums + nums
        
        max_ones_in_window = 0
        current_ones_in_window = 0

        for i in range(count_ones):
            current_ones_in_window += nums_extended[i]
        
        max_ones_in_window = current_ones_in_window

        for i in range(1, n):
            current_ones_in_window = current_ones_in_window - nums_extended[i - 1] + nums_extended[i + count_ones - 1]
            max_ones_in_window = max(max_ones_in_window, current_ones_in_window)

        min_swaps = count_ones - max_ones_in_window
        return min_swaps
