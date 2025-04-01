/**
 * @param {number} n
 * @return {number}
 */
function climbStairs(n) {
  if (n <= 2) {
    return n;
  }

  let oneStair = 1;
  let twoStairs = 2;
  for (let i = 3; i <= n; i++) {
    let current = oneStair + twoStairs;
    oneStair = twoStairs;
    twoStairs = current;
  }

  return twoStairs;
}