/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  nums.sort((a, b) => a - b);
  //   return nums;
  let ans = 0;
  for (let i = 0; i < nums.length; i++) {
    if (ans !== nums[i]) {
      return ans;
    }
    ans++;
  }
  return nums.length;
};