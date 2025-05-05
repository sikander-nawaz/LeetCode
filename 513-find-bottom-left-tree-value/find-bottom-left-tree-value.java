/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int findBottomLeftValue(TreeNode root) {
        if (root == null)
            return -1; // Or any other suitable default value to indicate an error

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int result = root.val;

        while (!queue.isEmpty()) {
            int size = queue.size();
            result = queue.peek().val; // Update the result with the leftmost node at each level

            for (int i = 0; i < size; i++) {
                TreeNode current = queue.poll();

                if (current.left != null) {
                    queue.offer(current.left);
                }

                if (current.right != null) {
                    queue.offer(current.right);
                }
            }
        }

        return result;
    }
}