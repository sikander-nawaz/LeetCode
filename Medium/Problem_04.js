// Given a string s. Return all the words vertically in the same order in which they appear in s.
// Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
// Each word would be put on only one column and that in one column there will be only one word.

// Example 1:
// Input: s = "HOW ARE YOU"
// Output: ["HAY","ORO","WEU"]
// Explanation: Each word is printed vertically.
//  "HAY"
//  "ORO"
//  "WEU"

// SOLUTION:

var printVertically = function (s) {
  let words = s.split(" ");
  let maxLength = Math.max(...words.map((word) => word.length));
  let charArrays = words.map((word) => word.split(""));
  let result = [];

  for (let i = 0; i < maxLength; i++) {
    let column = "";

    for (let j = 0; j < charArrays.length; j++) {
      column += i < charArrays[j].length ? charArrays[j][i] : " ";
    }

    result.push(column.trimRight());
  }

  return result;
};

let s = "HOW ARE YOU";
console.log(printVertically(s));
