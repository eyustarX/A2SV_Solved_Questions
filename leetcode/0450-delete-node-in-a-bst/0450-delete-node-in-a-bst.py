# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minValue(node):
            curr = node
            while curr.left:
                curr = curr.left
            
            return curr

        def deleteNode(node, key):
            if not node:
                return None
            
            if key < node.val:
                node.left = deleteNode(node.left, key)
            
            elif key > node.val:
                node.right = deleteNode(node.right, key)
            
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                temp = minValue(node.right)
                node.val = temp.val
                node.right = deleteNode(node.right, temp.val)

            return node
        
        return deleteNode(root, key)