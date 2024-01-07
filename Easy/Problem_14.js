// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:
// Input: s = "anagram", t = "nagaram"
// Output: true

// SOLUTION:

var isAnagram = function (s, t) {
  s = [...s].sort().join("");
  t = [...t].sort().join("");

  return s === t;
};

let s = "rat";
let t = "car";
console.log(isAnagram(s, t));
