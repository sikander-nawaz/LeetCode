/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function (nums) {
  let answer = [];

  for (let i = 0; i < nums.length; i++) {
    let counter = 0;

    for (let j = 0; j < nums.length; j++) {
      if (nums[i] > nums[j]) {
        counter++;
      }
    }
    answer.push(counter);
  }

  return answer
};