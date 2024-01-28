// You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
// Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

// Example 1:
// Input: nums = [1,2,3,1]
// Output: 4
// Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
// Total amount you can rob = 1 + 3 = 4.

// SOLUTION:

var rob = function (nums) {
  if (nums.length === 0) {
    return 0;
  } else if (nums.length <= 2) {
    return Math.max(...nums);
  } else {
    let evenSum = 0;
    let oddSum = 0;

    for (let i = 0; i < nums.length; i++) {
      if (i % 2 === 0) {
        evenSum += nums[i];
        evenSum = Math.max(evenSum, oddSum);
      } else {
        oddSum += nums[i];
        oddSum = Math.max(evenSum, oddSum);
      }
    }

    return Math.max(evenSum, oddSum);
  }
};

const nums = [2, 7, 9, 3, 1];
console.log(rob(nums));
