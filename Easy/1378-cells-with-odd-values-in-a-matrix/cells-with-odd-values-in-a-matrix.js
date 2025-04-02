/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} indices
 * @return {number}
 */
var oddCells = function (m, n, indices) {
  const row = Array(m).fill(0);
  const col = Array(n).fill(0);

  for (const [ri, ci] of indices) {
    row[ri]++;
    col[ci]++;
  }

  let count = 0;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      let value = row[i] + col[j];
      count += value % 2;
    }
  }

  return count;
};