class Solution:
    def findMaxK(self, nums):
        maximum = max(nums)
        for i in range(len(nums)):
            if -maximum in nums:
                return maximum
            else:
                nums.remove(maximum)
            if not nums:
                return -1
            maximum = max(nums)
        return maximum




         # take maximum positive value, 
        # find their negative 
        # return -1 if we've no positive maximum number
        # if negative available then reutn maximum
        # if negative not found then decerement value