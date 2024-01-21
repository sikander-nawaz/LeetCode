// Given a square matrix mat, return the sum of the matrix diagonals.
// Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

// Example 2:
// Input: mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
// Output: 8

// SOLUTION:

function diagonalSum(mat) {
  let leftSum = 0;
  let rightSum = 0;

  for (let i = 0; i < mat.length; i++) {
    leftSum += mat[i][i];
    rightSum += mat[i][n - 1 - i];
  }

  if (mat.length % 2 === 1) {
    let centerIndex = Math.floor(mat.length / 2);
    leftSum -= mat[centerIndex][centerIndex];
  }

  return leftSum + rightSum;
}

// Example usage:
let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
console.log(diagonalSum(matrix));
