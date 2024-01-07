// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
// We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
// You must solve this problem without using the library's sort function.

// Example 1:
// Input: nums = [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]

// SOLUTION:

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

let nums = [2, 0, 2, 1, 1, 0];
console.log(sortColors(nums));
