# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.result += 1
            
            return [d + 1 for d in left_distances + right_distances]
        
        self.result = 0
        dfs(root)
        return self.result
        