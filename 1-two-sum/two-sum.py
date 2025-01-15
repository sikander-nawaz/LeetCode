class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            number2 = target -nums[i]
            if number2 in hashMap:
                 return [hashMap[number2],i]
            else:
                 hashMap[nums[i]] = i