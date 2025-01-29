/**
 * @param {number[]} nums
 * @param {number[]} index
 * @return {number[]}
 */
var createTargetArray = function (nums, index) {
  let targetArray = [];
  for (let i = 0; i < nums.length; i++) {
    for (let j = i; j < index.length; j++) {
      targetArray.splice(index[j], 0, nums[i]);
      break;
    }
  }
  return targetArray;
};