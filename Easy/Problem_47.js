// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".

// Example 1:
// Input: strs = ["flower","flow","flight"]
// Output: "fl"

// SOLUTION:

var longestCommonPrefix = function (strs) {
  let ans = strs.join("").split("");

  return ans;
};

let strs = ["flower", "flow", "flight"];
console.log(longestCommonPrefix(strs));
