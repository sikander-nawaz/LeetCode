// There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.
// For each location indices[i], do both of the following:
// Increment all the cells on row ri.
// Increment all the cells on column ci.
// Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

// Example 1:
// Input: m = 2, n = 2, indices = [[1,1],[0,0]]
// Output: 0
// Explanation: Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.

// SOLUTION:

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

let m = 2;
let n = 3;
let indices = [
  [0, 1],
  [1, 1],
];

console.log(oddCells(m, n, indices));
