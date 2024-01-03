// Given an integer x, return true if x is a palindrome, and false otherwise.

// Example 1:
// Input: x = 121
// Output: true
// Explanation: 121 reads as 121 from left to right and from right to left.

// SOLUTION:

var isPalindrome = function (x) {
  let arr = x.toString().split("").reverse();
  let number = parseInt(arr.join(""));

  return x === number;
};

let x = -121;
console.log(isPalindrome(x));
