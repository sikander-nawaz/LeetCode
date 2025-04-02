/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function (nums) {
  let count = 0;

  nums.forEach((e) => {
    let lengthOfNumber = e.toString().length;
    if (lengthOfNumber % 2 === 0) {
      count++;
    }
  });

  return count;
};