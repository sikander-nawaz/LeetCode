// The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
// P   A   H   N
// A P L S I I G
// Y   I   R
// And then read line by line: "PAHNAPLSIIGYIR"
// Write the code that will take a string and make this conversion given a number of rows:
// string convert(string s, int numRows);

// Example 1:
// Input: s = "PAYPALISHIRING", numRows = 3
// Output: "PAHNAPLSIIGYIR"

// SOLUTION:

function convert(s, numRows) {
  if (numRows === 1 || numRows >= s.length) {
    return s;
  }

  let rows = new Array(numRows).fill("");
  let index = 0;
  let direction = 1;

  for (const char of s) {
    rows[index] += char;
    if (index === 0) {
      direction = 1;
    } else if (index === numRows - 1) {
      direction = -1;
    }
    index += direction;
  }

  return rows.join("");
}

let inputString = "PAYPALISHIRING";
let numRows = 3;
console.log(convert(inputString, numRows));
