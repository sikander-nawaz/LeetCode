// You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

// Example 1:
// Input: n = 2
// Output: 2
// Explanation: There are two ways to climb to the top.
// 1. 1 step + 1 step
// 2. 2 steps

// SOLUTION:

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

let n = 2;
console.log(climbStairs(n));
