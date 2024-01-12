// Given a signed 32-bit integer x, return x with its digits ans. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

// Example 1:
// Input: x = 123
// Output: 321

// SOLUTION:

var reverse = function (x) {
  let str1 = x.toString();
  let arr = str1.split("");
  //   console.log(arr);
  let reverse = arr.reverse();
  //   console.log(ans);
  let str = reverse.join("");
  //   console.log(str);
  let ans = x >= 0 ? parseInt(str) : -parseInt(str);
  if (ans < Math.pow(-2, 31) || ans > Math.pow(2, 31) - 1) {
    return 0;
  } else {
    return ans;
  }
};

let x = 1534236469;
console.log(reverse(x));
