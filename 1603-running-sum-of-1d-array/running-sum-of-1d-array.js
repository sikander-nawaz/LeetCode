/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function (nums) {
  let runningSum = 0;
  let result = [];

  for (let i = 0; i < nums.length; i++) {
    runningSum += nums[i];
    result.push(runningSum);
  }
  return result;
};