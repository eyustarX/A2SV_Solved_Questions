# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            return path(node, targetSum) + dfs(node.left) + dfs(node.right)
        
        def path(node, target):
            if not node:
                return 0
            
            count = 0

            count = 1 if node.val == target else 0

            count += path(node.left, target - node.val)
            count += path(node.right, target - node.val)

            return count
        
        return dfs(root)