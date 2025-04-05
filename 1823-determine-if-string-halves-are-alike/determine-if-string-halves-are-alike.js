/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function (s) {
  let half = s.length / 2;

  let a = s.slice(0, half);
  let b = s.slice(half);

  let countA = 0;
  for (const e of a) {
    if (
      e == "a" ||
      e == "e" ||
      e == "i" ||
      e == "o" ||
      e == "u" ||
      e == "A" ||
      e == "E" ||
      e == "I" ||
      e == "O" ||
      e == "U"
    ) {
      countA++;
    }
  }

  let countB = 0;
  for (const e of b) {
    if (
      e == "a" ||
      e == "e" ||
      e == "i" ||
      e == "o" ||
      e == "u" ||
      e == "A" ||
      e == "E" ||
      e == "I" ||
      e == "O" ||
      e == "U"
    ) {
      countB++;
    }
  }
  return countA === countB;
};