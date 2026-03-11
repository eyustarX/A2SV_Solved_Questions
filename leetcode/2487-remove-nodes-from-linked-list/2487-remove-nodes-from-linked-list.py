# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head

        while curr:
            while stack and stack[-1][0] < curr.val:
                stack.pop()
            
            stack.append((curr.val,curr))
            curr = curr.next
        
        for i in range(len(stack) - 1):
            stack[i][1].next = stack[i + 1][1]
        
        stack[-1][1].next = None

        return stack[0][1]