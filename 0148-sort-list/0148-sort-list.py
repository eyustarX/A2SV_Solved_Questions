# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        stack.sort()
        node = ListNode(stack[0])
        root = node
        for i in range(1, len(stack)):
            root.next = ListNode(stack[i])
            root = root.next
            
        return node