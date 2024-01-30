// Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
// If target is not found in the array, return [-1, -1].
// You must write an algorithm with O(log n) runtime complexity.

// Example 1:
// Input: nums = [5,7,7,8,8,10], target = 8
// Output: [3,4]

function searchRange(nums, target) {
  if (!nums.includes(target)) {
    return [-1, -1];
  } else {
    let firstPosition = nums.indexOf(target);
    let lastPosition = nums.lastIndexOf(target);

    return [firstPosition, lastPosition];
  }
}

let nums = [5, 7, 7, 8, 8, 10];
let target = 8;

console.log(searchRange(nums, target));
