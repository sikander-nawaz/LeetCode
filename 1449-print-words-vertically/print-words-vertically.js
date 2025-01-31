/**
 * @param {string} s
 * @return {string[]}
 */
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