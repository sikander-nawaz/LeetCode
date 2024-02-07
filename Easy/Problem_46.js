// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

// Example 2:
// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [9,4]
// Explanation: [4,9] is also accepted.

// SOLUTION:

var intersection = function (nums1, nums2) {
  let digits = [];

  for (let i = 0; i < nums1.length; i++) {
    for (let j = 0; j < nums2.length; j++) {
      if (nums1[i] === nums2[j]) {
        digits.push(nums1[i]);
      }
    }
  }

  let ans = new Set(digits);
  return [...ans];
};

let nums1 = [4, 9, 5];
let nums2 = [9, 4, 9, 8, 4];

console.log(intersection(nums1, nums2));
