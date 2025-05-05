class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def get_mapped_value(num: int) -> int:
            mapped_digits = [str(mapping[int(digit)]) for digit in str(num)]
            return int(''.join(mapped_digits))
        
        mapped_nums = [(get_mapped_value(num), num) for num in nums]
        
        mapped_nums.sort(key=lambda x: x[0])
        
        return [num for _, num in mapped_nums]