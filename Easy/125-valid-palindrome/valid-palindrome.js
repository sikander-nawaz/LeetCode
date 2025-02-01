/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  let cleanWords = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
  return cleanWords === cleanWords.split("").reverse().join("");
};