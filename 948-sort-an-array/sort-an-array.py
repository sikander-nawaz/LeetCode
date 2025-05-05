class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        def merge(left: List[int], right: List[int]) -> List[int]:
            sorted_array = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_array.append(left[i])
                    i += 1
                else:
                    sorted_array.append(right[j])
                    j += 1
            
            # Append remaining elements, if any
            while i < len(left):
                sorted_array.append(left[i])
                i += 1
            while j < len(right):
                sorted_array.append(right[j])
                j += 1
                
            return sorted_array
        
        def merge_sort(nums: List[int]) -> List[int]:
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            
            return merge(left, right)
        
        return merge_sort(nums)
