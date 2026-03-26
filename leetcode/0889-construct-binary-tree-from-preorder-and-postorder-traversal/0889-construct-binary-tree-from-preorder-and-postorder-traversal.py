# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(pre, post):
            if not pre:
                return None
            
            root = TreeNode(pre[0])

            if len(pre) == 1:
                return root

            index = post.index(pre[1])

            root.left = build(pre[1:index + 2], post[:index + 1])
            root.right = build(pre[index + 2:], post[index + 1: -1])

            return root
        
        return build(preorder,postorder)