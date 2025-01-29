/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function (sentence) {
  sentence = sentence.toLowerCase();
  if (new Set(sentence).size === 26) {
    return true;
  } else {
    return false;
  }
};