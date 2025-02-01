/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  digits = BigInt(digits.join(""));
  let ans = digits + 1n;
  let finalAns = ans.toString().split("");
  const numArray = finalAns.map(function (char) {
    return parseInt(char, 10);
  });
  return numArray;
};