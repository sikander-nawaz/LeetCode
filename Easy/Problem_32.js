// You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
// Merge nums1 and nums2 into a single array sorted in non-decreasing order.
// The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

// Example 1:
// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
// Output: [1,2,2,3,5,6]
// Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
// The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

// SOLUTION:

function merge(nums1, m, nums2, n) {
  nums1.splice(m, n, ...nums2);
  return nums1.sort((a, b) => a - b);
}

let nums1 = [
  -10, -10, -9, -9, -9, -8, -8, -7, -7, -7, -6, -6, -6, -6, -6, -6, -6, -5, -5,
  -5, -4, -4, -4, -3, -3, -2, -2, -1, -1, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5,
  6, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0,
];
let m = 55;
let nums2 = [
  -10, -10, -9, -9, -9, -9, -8, -8, -8, -8, -8, -7, -7, -7, -7, -7, -7, -7, -7,
  -6, -6, -6, -6, -5, -5, -5, -5, -5, -4, -4, -4, -4, -4, -3, -3, -3, -2, -2,
  -2, -2, -2, -2, -2, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2,
  2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7,
  7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
];
let n = 99;

console.log(merge(nums1, m, nums2, n));
