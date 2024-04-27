# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.


# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# SOLUTION:

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} 
        def rec (index, exp_result):
            
            if index == len(nums):

                if exp_result == target:
                    return 1

                return 0

            if (index , exp_result) in memo:
                return memo[(index, exp_result)]

            result = rec(index + 1, exp_result + nums[index]) + rec(index + 1, exp_result - nums[index])
            memo[(index, exp_result)] = result

            return result

        return rec(0, 0)