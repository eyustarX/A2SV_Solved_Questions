# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        
        while curr:
            count += 1
            curr = curr.next
        k = count // 2 
        node = head
        for _ in range(k):
            node = node.next

        return node