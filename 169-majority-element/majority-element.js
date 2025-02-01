/**
 * @param {number[]} nums
 * @return {number}
 */
function majorityElement(nums) {
  let index = nums[0];
  let count = 1;

  for (let i = 1; i < nums.length; i++) {
    if (count === 0) {
      index = nums[i];
      count = 1;
    } else if (nums[i] === index) {
      count++;
    } else {
      count--;
    }
  }

  return index;
}