// Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.
// A substring is a contiguous sequence of characters within a string.

// Example 1:
// Input: patterns = ["a","abc","bc","d"], word = "abc"
// Output: 3
// Explanation:
// - "a" appears as a substring in "abc".
// - "abc" appears as a substring in "abc".
// - "bc" appears as a substring in "abc".
// - "d" does not appear as a substring in "abc".
// 3 of the strings in patterns appear as a substring in word.

// SOLUTION:

var numOfStrings = function (patterns, word) {
  let output = 0;

  for (const e of patterns) {
    if (word.includes(e)) {
      output++;
    }
  }

  return output;
};

let patterns = ["a", "abc", "bc", "d"];
let word = "abc";
console.log(numOfStrings(patterns, word));
