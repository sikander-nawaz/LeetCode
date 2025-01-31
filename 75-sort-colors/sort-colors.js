/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {
  let red = 0;
  let white = 0;
  let blue = 0;

  for (const val of nums) {
    if (val === 0) {
      red++;
    } else if (val === 1) {
      white++;
    } else {
      blue++;
    }
  }

  let i = 0;

  for (let j = 0; j < red; j++) {
    nums[i++] = 0;
  }

  for (let j = 0; j < white; j++) {
    nums[i++] = 1;
  }

  for (let j = 0; j < blue; j++) {
    nums[i++] = 2;
  }

  return nums;
};