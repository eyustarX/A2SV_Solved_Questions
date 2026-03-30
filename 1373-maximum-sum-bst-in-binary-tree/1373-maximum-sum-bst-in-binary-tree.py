# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0

        def dfs(node):
            if not node:
                return True, float("inf"), float("-inf"), 0
            
            left_BST, left_left, left_right, left_sum =  dfs(node.left)
            right_BST, right_left, right_right, right_sum = dfs(node.right)

            if left_BST and right_BST and left_right < node.val < right_left:
                total = node.val + left_sum + right_sum
                self.max_sum = max(self.max_sum, total)

                return True, min(left_left, node.val), max(right_right, node.val), total
            
            else:
                return False, 0, 0, 0
        
        dfs(root)
        return self.max_sum