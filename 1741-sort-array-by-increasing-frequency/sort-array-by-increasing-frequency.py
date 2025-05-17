class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        freq_list = [(num, count) for num, count in freq.items()]
        
        freq_list.sort(key=lambda x: (x[1], -x[0]))
        
        result = []
        for num, count in freq_list:
            result.extend([num] * count)
        
        return result
