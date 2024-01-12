// You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
// Return the merged string.

// Example 1:
// Input: word1 = "abc", word2 = "pqr"
// Output: "apbqcr"
// Explanation: The merged string will be merged as so:
// word1:  a   b   c
// word2:    p   q   r
// merged: a p b q c r

// SOLUTION:

var mergeAlternately = function (word1, word2) {
  let ans = [];

  for (let i = 0; i < Math.max(word1.length, word2.length); i++) {
    if (i < word1.length) {
      ans.push(word1[i]);
    }

    if (i < word2.length) {
      ans.push(word2[i]);
    }
  }

  return ans.join("");
};

let word1 = "abc";
let word2 = "pqr";
console.log(mergeAlternately(word1, word2));
