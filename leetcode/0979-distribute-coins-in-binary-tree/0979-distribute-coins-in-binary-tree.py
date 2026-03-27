# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def coins(node):
            if not node:
                return 0

            left = coins(node.left)
            right = coins(node.right)

            self.moves += abs(left) + abs(right)

            return node.val + left + right -1
        
        coins(root)

        return self.moves