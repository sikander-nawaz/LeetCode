// You are given two strings order and s. All the characters of order are unique
// and were sorted in some custom order previously.
// Permute the characters of s so that they match the order that order was
// sorted. More specifically, if a character x occurs before a character y in
// order, then x should occur before y in the permuted string.
// Return any permutation of s that satisfies this property.

// Example 1:
// Input: order = "cba", s = "abcd"
// Output: "cbad"
// Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c"
// should be "c", "b", and "a".
// Since "d" does not appear in order, it can be at any position in the returned
// string. "dcba", "cdba", "cbda" are also valid outputs.

// SOLUTION:
class Solution {

     public class Problem_11 (String order, String s){

     int alpha[] = new int[26];for(
     int i = 0;i<s.length();i++)alpha[s.charAt(i)-97]++;
     String ans = "";

     for(
     int i = 0;i<order.length();i++)
     {
          ans += ("" + String.valueOf(order.charAt(i)).repeat(alpha[order.charAt(i) - 97]));
          alpha[order.charAt(i) - 97] = 0;
     }

     for(
     int i = 0;i<26;i++)
     {
          ans += ("" + (char) (i + 97)).repeat(alpha[i]);
     }

     return ans;
}
}