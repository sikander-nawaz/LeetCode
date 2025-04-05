/**
 * @param {string[]} patterns
 * @param {string} word
 * @return {number}
 */
var numOfStrings = function (patterns, word) {
  let output = 0;

  for (const e of patterns) {
    if (word.includes(e)) {
      output++;
    }
  }

  return output;
};