/**
 * @param {number[][]} mat
 * @return {number}
 */
function diagonalSum(mat) {
  let leftSum = 0;
  let rightSum = 0;
  let n = mat.length;

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