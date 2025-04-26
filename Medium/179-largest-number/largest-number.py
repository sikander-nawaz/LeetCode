class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = []
        if set(nums) == {0}:
            return "0"
        for i in range(len(nums)):
            c = nums[i] / ( 10 ** len(str(nums[i]))-1)
            res.append((nums[i],c))
        res.sort(key= lambda x:x[1],reverse=True)

        result = ''
        for num,den in res:
            result += str(num)
        return result