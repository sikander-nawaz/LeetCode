// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
// Given a string s, return true if it is a palindrome, or false otherwise.

// Example 1:
// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.

// SOLUTION:

var isPalindrome = function (s) {
  let cleanWords = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
  return cleanWords === cleanWords.split("").reverse().join("");
};

let s = "A man, a plan, a canal: Panama";
console.log(isPalindrome(s));
