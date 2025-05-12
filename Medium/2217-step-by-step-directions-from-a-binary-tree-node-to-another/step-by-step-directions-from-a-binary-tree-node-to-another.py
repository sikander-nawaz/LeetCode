# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        def find_path(root, value):
            if not root:
                return None
            if root.val == value:
                return ""
            left_path = find_path(root.left, value)
            if left_path is not None:
                return "L" + left_path
            right_path = find_path(root.right, value)
            if right_path is not None:
                return "R" + right_path
            return None
        
        path_to_start = find_path(root, startValue)
        path_to_dest = find_path(root, destValue)
        
        i = 0
        while i < len(path_to_start) and i < len(path_to_dest) and path_to_start[i] == path_to_dest[i]:
            i += 1
        
        steps_up = "U" * (len(path_to_start) - i)
        steps_down = path_to_dest[i:]
        
        return steps_up + steps_down
        