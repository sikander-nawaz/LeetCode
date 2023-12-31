// Given an integer number n, return the difference between the product of its digits and the sum of its digits.

// Example 1:
// Input: n = 234
// Output: 15
// Explanation:
// Product of digits = 2 * 3 * 4 = 24
// Sum of digits = 2 + 3 + 4 = 9
// Result = 24 - 9 = 15

// SOLUTION:

var subtractProductAndSum = function (n) {
  let str = n.toString();
  let product = 1;
  let sum = 0;
  for (const i of str) {
    product *= parseInt(i);
    sum += parseInt(i);
  }
  return product - sum;
};

let n = 4421;
console.log(subtractProductAndSum(n));
