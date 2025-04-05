/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function (word, ch) {
  let index = word.indexOf(ch) + 1;
  let firstReverseWords = word.substring(0, index).split("").reverse().join("");
  let lastWords = word.substring(index);

  return firstReverseWords + lastWords;
};