/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  s = s.trim();
  s = s.split(" ");
  let last = s.pop();
  return last.length;
};