/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function (nums) {
  let product = 1;

  for (let i = 0; i < nums.length; i++) {
    product *= nums[i];
  }

  return product < 0 ? -1 : product > 0 ? 1 : 0;
};