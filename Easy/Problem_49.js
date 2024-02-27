// You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
// Given the integer n, return the number of complete rows of the staircase you will build.

// Example 1:
// Input: n = 5
// Output: 2
// Explanation: Because the 3rd row is incomplete, we return 2.


// SOLUTION:
class Solution {
     public int arrangeCoins(int n) {
         if (n < 0) {
             throw new IllegalArgumentException("Only positive numbers are allowed");
         }
         return (int) (Math.sqrt(2 * (long) n + 0.25) - 0.5);
     }
}

