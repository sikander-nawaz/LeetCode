class Solution {
     public int arrangeCoins(int n) {
         if (n < 0) {
             throw new IllegalArgumentException("Only positive numbers are allowed");
         }
         return (int) (Math.sqrt(2 * (long) n + 0.25) - 0.5);
     }
}