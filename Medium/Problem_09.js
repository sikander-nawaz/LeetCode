// Given a string s, find the length of the longest substring without repeating characters.

// Example 1:
// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.

// SOLUTION:

var lengthOfLongestSubstring = function (s) {
  const set = new Set();
  let longest = 0;
  let i = 0;
  let j = 0;

  while (i < s.length && j < s.length) {
    if (!set.has(s[j])) {
      set.add(s[j]);
      longest = Math.max(longest, j - i + 1);
      j += 1;
    } else {
      set.delete(s[i]);
      i += 1;
    }
  }
  return longest;
};

let s = "abcabcbb";
console.log(lengthOfLongestSubstring(s));
