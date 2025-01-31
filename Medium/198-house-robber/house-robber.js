/**
 * @param {number[]} nums
 * @return {number}
 */
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