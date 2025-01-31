/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
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