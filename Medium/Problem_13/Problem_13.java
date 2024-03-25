// Given an array nums of distinct integers, return all the possible
// permutations. You can return the answer in any order.

// Example 1:
// Input: nums = [1,2,3]
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

// SOLUTION:

import java.util.ArrayList;
import java.util.List;

/**
 * Problem_13
 */
class Problem_13 {
     public List<List<Integer>> permute(int[] nums) {
          List<List<Integer>> result = new ArrayList<>();
          if (nums.length == 1) {
               List<Integer> perm = new ArrayList<>();
               perm.add(nums[0]);
               result.add(perm);
               return result;
          }
          for (int i = 0; i < nums.length; i++) {
               int n = nums[i];
               int[] remainingNums = new int[nums.length - 1];
               int index = 0;
               for (int j = 0; j < nums.length; j++) {
                    if (j != i) {
                         remainingNums[index++] = nums[j];
                    }
               }
               List<List<Integer>> perms = permute(remainingNums);
               for (List<Integer> perm : perms) {
                    perm.add(n);
               }
               result.addAll(perms);
          }
          return result;
     }
}