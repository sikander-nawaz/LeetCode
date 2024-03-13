// Given a positive integer n, find the pivot integer x such that:

// The sum of all elements between 1 and x inclusively equals the sum of all
// elements between x and n inclusively.
// Return the pivot integer x. If no such integer exists, return -1. It is
// guaranteed that there will be at most one pivot index for the given input.

// public class Problem {
// int sum = 0;
// for(int i = 1;i<=n;i++){
// sum += i;
// };

// int sum1 = 0;
// for( int i = 1;i<=n;i++){
// sum1 += i;
// if (sum1 == (sum - sum1 + i)) {
// return i;
// }
// }
// return-1;
// }
