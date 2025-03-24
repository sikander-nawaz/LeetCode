class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        count_ones = sum(nums)
        
        # If there are no 1's or all are 1's, no swap needed
        if count_ones == 0 or count_ones == n:
            return 0
        
        # Create a circular version of the array
        nums_extended = nums + nums
        
        # Find the max number of 1's in any window of size count_ones
        max_ones_in_window = 0
        current_ones_in_window = 0
        
        # Initialize the first window
        for i in range(count_ones):
            current_ones_in_window += nums_extended[i]
        
        max_ones_in_window = current_ones_in_window
        
        # Slide the window across the extended array
        for i in range(1, n):
            current_ones_in_window = current_ones_in_window - nums_extended[i - 1] + nums_extended[i + count_ones - 1]
            max_ones_in_window = max(max_ones_in_window, current_ones_in_window)
        
        # Minimum swaps needed to group all 1's together
        min_swaps = count_ones - max_ones_in_window
        return min_swaps
