var maximumProduct = function (nums) {
  let positive = nums.map(Math.abs);
  let sort = positive.sort();
  return sort[sort.length - 1] * sort[sort.length - 2] * sort[sort.length - 3];
};

let nums = [-1, -2, -3];

console.log(maximumProduct(nums));
