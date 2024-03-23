// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

// Example 1:
// Input: root = [3,9,20,null,null,15,7]
// Output: [[3],[9,20],[15,7]]

package Medium.Problem_12;

import java.util.ArrayList;
import java.util.List;
// import javax.swing.tree.TreeNode;

//   Definition for a binary tree node.
public class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;

     TreeNode() {
     }

     TreeNode(int val) {
          this.val = val;
     }

     TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
     }
}

public class Problem_12 {
     public List<List<Integer>> levelOrder(TreeNode root) {
          List<List<Integer>> ans = new ArrayList<>();

          traverse(root, 0, ans);

          return ans;
     }

     private void traverse(TreeNode node, int index, List<List<Integer>> ans) {
          if (node == null) {
               return;
          }

          if (ans.size() <= index) {
               List<Integer> subLevel = new ArrayList<>();
               subLevel.add(node.val);
               ans.add(subLevel);
          } else {
               ans.get(index).add(node.val);
          }

          traverse(node.left, index + 1, ans);
          traverse(node.right, index + 1, ans);
     }
}
