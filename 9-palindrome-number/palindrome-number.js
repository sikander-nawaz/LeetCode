/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  let arr = x.toString().split("").reverse();
  let number = parseInt(arr.join(""));

  return x === number;
};