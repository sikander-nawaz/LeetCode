class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        R, L = 0, len(nums)-1
        while R <= L:
            MID = R + (L-R)//2
            if nums[MID] == target:
                return MID
            elif  nums[MID] > target:
                L = MID - 1
            else:
                R = MID + 1
            if R > L:
                return R
